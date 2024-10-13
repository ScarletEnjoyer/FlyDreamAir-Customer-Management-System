from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT
from ui.customer.multiSelectDialog import MultiSelectDialog

from api.flightApi import get_available_seats, remove_seat
from api.serviceApi import get_services
from api.reservationApi import book_flight


class FlightItemWidget(QWidget):
    update_signal = pyqtSignal()

    def __init__(self, parent, i, flight, customer):
        super().__init__(parent)
        self.flight = flight
        self.customer = customer
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName('flight_item_widget')
        if i % 2 == 0:
            self.background_color = 'background-color: rgb(181,210,230);'
        else:
            self.background_color = 'background-color: rgb(231,232,240);'
        self.setStyleSheet(f'QWidget#flight_item_widget {{{self.background_color}}}')
        self.item_layout = QVBoxLayout()
        self.item_layout.setSpacing(5)

        self.line_1 = QWidget(self)
        self.line_1_layout = QHBoxLayout()
        self.flight_number_label = QLabel(f'Flight number: {flight.flight_number}', self.line_1)
        self.flight_number_label.setFont(LABEL_FONT)
        self.book_button = QPushButton('Book', self.line_1)
        self.book_button.setFont(LABEL_FONT)
        self.book_button.setMaximumWidth(100)
        self.book_button.clicked.connect(self.book_button_clicked)
        self.line_1_layout.addWidget(self.flight_number_label)
        self.line_1_layout.addWidget(self.book_button)
        self.line_1.setLayout(self.line_1_layout)
        self.item_layout.addWidget(self.line_1)

        self.line_2 = QWidget(self)
        self.line_2_layout = QVBoxLayout()
        from_str = f'From {flight.country_from}'
        if flight.admin1_from != '':
            from_str += f', {flight.admin1_from}'
        if flight.admin2_from != '':
            from_str += f', {flight.admin2_from}'
        to_str = f'To {flight.country_to}'
        if flight.admin1_to != '':
            to_str += f', {flight.admin1_to}'
        if flight.admin2_to != '':
            to_str += f', {flight.admin2_to}'
        self.from_label = QLabel(from_str, self.line_2)
        self.from_label.setFont(LABEL_FONT)
        self.line_2_layout.addWidget(self.from_label)
        self.to_label = QLabel(to_str, self.line_2)
        self.to_label.setFont(LABEL_FONT)
        self.line_2_layout.addWidget(self.to_label)
        self.line_2.setLayout(self.line_2_layout)
        self.item_layout.addWidget(self.line_2)

        self.line_3 = QWidget()
        self.line_3_layout = QHBoxLayout()
        self.departure_time_label = QLabel(f'Departure time: {flight.departure_time.toString("yyyy-MM-dd HH:mm:ss")}')
        self.departure_time_label.setFont(LABEL_FONT)
        self.line_3_layout.addWidget(self.departure_time_label)
        self.arrival_time_label = QLabel(f'Arrival time: {flight.arrival_time.toString("yyyy-MM-dd HH:mm:ss")}')
        self.arrival_time_label.setFont(LABEL_FONT)
        self.line_3_layout.addWidget(self.arrival_time_label)
        self.line_3.setLayout(self.line_3_layout)
        self.item_layout.addWidget(self.line_3)

        self.line_4 = QWidget()
        self.line_4_layout = QHBoxLayout()
        self.available_seats_label = QLabel('Available seats:', self.line_4)
        self.available_seats_label.setFont(LABEL_FONT)
        self.line_4_layout.addWidget(self.available_seats_label)
        for seat_class in flight.seats.keys():
            if flight.seats[seat_class]['count'] != 0:
                label = QLabel(f"{seat_class}: {len(flight.seats[seat_class]['available_seats'])}/{flight.seats[seat_class]['count']}")
                label.setFont(LABEL_FONT)
                self.line_4_layout.addWidget(label)
        self.line_4.setLayout(self.line_4_layout)
        self.item_layout.addWidget(self.line_4)

        self.setMinimumHeight(200)
        self.setFixedHeight(200)
        self.setLayout(self.item_layout)

    def book_button_clicked(self):
        available_seats = get_available_seats(self.flight)
        if len(available_seats) == 0:
            QMessageBox.critical(self, 'Error', 'There are no seats available on this flight!')
            return
        seat_classes_and_unit_price = []
        for seat_class in available_seats.keys():
            seat_classes_and_unit_price.append(f'{seat_class} ({available_seats[seat_class]["unit_price"]} AUD)')

        selected_seat_class_and_unit_price, ok = QInputDialog.getItem(self, "", "Please select seat class:", seat_classes_and_unit_price, 0, False)
        if not ok or not selected_seat_class_and_unit_price:
            return
        selected_seat_class = ' '.join(selected_seat_class_and_unit_price.split(' ')[:2])
        selected_seat_class_price = available_seats[selected_seat_class]['unit_price']
        available_seats = [str(seat) for seat in available_seats[selected_seat_class]['available_seats']]

        selected_seat, ok = QInputDialog.getItem(self, "", "Please select a seat:", available_seats, 0, False)
        if not ok or not selected_seat:
            return
        selected_seat = int(selected_seat)
        all_services = get_services()
        all_servers_str = []
        for service in all_services:
            all_servers_str.append(f'{service.name}, unit price:{service.unit_price} AUD')
        dialog = MultiSelectDialog(self, all_servers_str)
        selected_service_strs = []
        if dialog.exec_() == QDialog.Accepted:
            selected_service_strs = dialog.get_selected_options()
        selected_services = []
        for service in all_services:
            if f'{service.name}, unit price:{service.unit_price} AUD' in selected_service_strs:
                selected_services.append(service)

        total_price = selected_seat_class_price
        for service in selected_services:
            total_price += service.unit_price
        reply = QMessageBox.question(self, '', f'You need to pay {total_price} AUD for the flight and services. Pay or not?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply != QMessageBox.Yes:
            return
        remove_seat(self.flight.flight_number, selected_seat_class, selected_seat)
        book_flight(self.customer.username, self.flight, selected_seat_class, selected_seat, selected_services)
        QMessageBox.information(self, 'Information','Flight booked successfully!')
        self.update_signal.emit()
