from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal
from ui.constant import LABEL_FONT
from api.reservationApi import cancel_reservation


class ReservationItemWidget(QWidget):
    cancel_signal = pyqtSignal()

    def __init__(self, parent, i, reservation):
        super().__init__(parent)
        self.reservation = reservation
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName('reservation_item_widget')
        if i % 2 == 0:
            self.background_color = 'background-color: rgb(181,210,230);'
        else:
            self.background_color = 'background-color: rgb(231,232,240);'
        self.setStyleSheet(f'QWidget#reservation_item_widget {{{self.background_color}}}')
        self.item_layout = QVBoxLayout()
        self.item_layout.setSpacing(5)

        self.line_1 = QWidget(self)
        self.line_1_layout = QHBoxLayout()
        self.flight_number_label = QLabel(f'Flight number: {self.reservation.flight.flight_number}', self.line_1)
        self.flight_number_label.setFont(LABEL_FONT)

        self.cancel_button = QPushButton('Cancel', self.line_1)
        self.cancel_button.setFont(LABEL_FONT)
        self.cancel_button.setMaximumWidth(100)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

        self.view_services_button = QPushButton('View services', self.line_1)
        self.view_services_button.setFont(LABEL_FONT)
        self.view_services_button.setMaximumWidth(150)
        self.view_services_button.clicked.connect(self.view_services_button_clicked)
        self.line_1_layout.addWidget(self.flight_number_label)
        self.line_1_layout.addWidget(self.cancel_button)
        self.line_1_layout.addWidget(self.view_services_button)
        self.line_1.setLayout(self.line_1_layout)
        self.item_layout.addWidget(self.line_1)

        self.line_2 = QWidget(self)
        self.line_2_layout = QVBoxLayout()
        from_str = f'From {self.reservation.flight.country_from}'
        if self.reservation.flight.admin1_from != '':
            from_str += f', {self.reservation.flight.admin1_from}'
        if self.reservation.flight.admin2_from != '':
            from_str += f', {self.reservation.flight.admin2_from}'
        to_str = f'To {self.reservation.flight.country_to}'
        if self.reservation.flight.admin1_to != '':
            to_str += f', {self.reservation.flight.admin1_to}'
        if self.reservation.flight.admin2_to != '':
            to_str += f', {self.reservation.flight.admin2_to}'
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
        self.departure_time_label = QLabel(f'Departure time: {self.reservation.flight.departure_time.toString("yyyy-MM-dd HH:mm:ss")}')
        self.departure_time_label.setFont(LABEL_FONT)
        self.line_3_layout.addWidget(self.departure_time_label)
        self.arrival_time_label = QLabel(f'Arrival time: {self.reservation.flight.arrival_time.toString("yyyy-MM-dd HH:mm:ss")}')
        self.arrival_time_label.setFont(LABEL_FONT)
        self.line_3_layout.addWidget(self.arrival_time_label)
        self.line_3.setLayout(self.line_3_layout)
        self.item_layout.addWidget(self.line_3)

        self.line_4 = QWidget()
        self.line_4_layout = QHBoxLayout()

        self.seat_class_label = QLabel(f'Seat class: {self.reservation.selected_seat_class}', self.line_4)
        self.seat_class_label.setFont(LABEL_FONT)
        self.line_4_layout.addWidget(self.seat_class_label)
        self.seat_label = QLabel(f'Seat:{self.reservation.selected_seat}', self.line_4)
        self.seat_label.setFont(LABEL_FONT)
        self.line_4_layout.addWidget(self.seat_label)
        self.line_4.setLayout(self.line_4_layout)
        self.item_layout.addWidget(self.line_4)
        self.setMinimumHeight(200)
        self.setFixedHeight(200)
        self.setLayout(self.item_layout)

    def cancel_button_clicked(self):
        reply = QMessageBox.question(self, '', 'Do you really want to cancel the reservation?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply != QMessageBox.Yes:
            return
        cancel_reservation(self.reservation)
        QMessageBox.information(self, 'Information', 'cancel reservation successfully!')
        self.cancel_signal.emit()

    def view_services_button_clicked(self):
        services = self.reservation.services
        if len(services) == 0:
            QMessageBox.information(self, 'Information', 'You have not ordered any service.')
        else:
            services_str = ', '.join([service.name for service in services])
            QMessageBox.information(self, 'Information', f'Services: {services_str}')
