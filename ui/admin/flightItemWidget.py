from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT
from api.flightApi import remove_flight


class FlightItemWidget(QWidget):
    remove_signal = pyqtSignal()

    def __init__(self, parent, i, flight):
        super().__init__(parent)
        self.flight = flight
        self.parent = parent
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
        self.remove_button = QPushButton('Remove', self.line_1)
        self.remove_button.setFont(LABEL_FONT)
        self.remove_button.setMaximumWidth(100)
        self.remove_button.clicked.connect(self.remove_button_clicked)
        self.line_1_layout.addWidget(self.flight_number_label)
        self.line_1_layout.addWidget(self.remove_button)
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

    def remove_button_clicked(self):
        remove_flight(self.flight)
        self.remove_signal.emit()
