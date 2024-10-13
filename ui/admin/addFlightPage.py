from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT
from ui.commonViews.inputFlightNumberWidget import InputFlightNumberWidget
from ui.commonViews.selectLocationWidget import SelectLocationWidget
from ui.commonViews.selectDateTimeWidget import SelectDateTimeWidget

from api.flightApi import *


class AddFlightPage(QWidget):
    def __init__(self, admin_main_page):
        super().__init__(admin_main_page)
        self.setObjectName('add_flights_page')
        self.setStyleSheet('QWidget#add_flights_page {background-color: white;}')
        self.main_layout = QVBoxLayout()

        self.input_flight_number_widget = InputFlightNumberWidget(self, "Flight number:", "Two capital letters and three digits. e.g. AA123")
        self.main_layout.addWidget(self.input_flight_number_widget)

        self.select_origin_location_widget = SelectLocationWidget(self, 'From:')
        self.main_layout.addWidget(self.select_origin_location_widget)

        self.select_destination_location_widget = SelectLocationWidget(self, 'To:')
        self.main_layout.addWidget(self.select_destination_location_widget)

        time_widget = QWidget(self)
        time_layout = QHBoxLayout()
        self.select_departure_time_widget = SelectDateTimeWidget(time_widget, 'Departure time:')
        time_layout.addWidget(self.select_departure_time_widget)

        self.select_arrival_time_widget = SelectDateTimeWidget(time_widget, 'Arrival time:')
        time_layout.addWidget(self.select_arrival_time_widget)
        time_widget.setLayout(time_layout)
        self.main_layout.addWidget(time_widget)

        space_widget = QWidget(self)
        space_layout = QHBoxLayout()

        economy_class_label = QLabel('Economy class:', space_widget)
        economy_class_label.setFont(LABEL_FONT)
        space_layout.addWidget(economy_class_label)

        self.economy_class_spinbox = QSpinBox(space_widget)
        self.economy_class_spinbox.setFont(LABEL_FONT)
        self.economy_class_spinbox.setRange(0, 100)
        self.economy_class_spinbox.setValue(0)
        space_layout.addWidget(self.economy_class_spinbox)

        business_class_label = QLabel('Business class:', space_widget)
        business_class_label.setFont(LABEL_FONT)
        space_layout.addWidget(business_class_label)

        self.business_class_spinbox = QSpinBox(space_widget)
        self.business_class_spinbox.setFont(LABEL_FONT)
        self.business_class_spinbox.setRange(0, 100)
        self.business_class_spinbox.setValue(0)
        space_layout.addWidget(self.business_class_spinbox)

        first_class_label = QLabel('First class:', space_widget)
        first_class_label.setFont(LABEL_FONT)
        space_layout.addWidget(first_class_label)

        self.first_class_spinbox = QSpinBox(space_widget)
        self.first_class_spinbox.setFont(LABEL_FONT)
        self.first_class_spinbox.setRange(0, 100)
        self.first_class_spinbox.setValue(0)
        space_layout.addWidget(self.first_class_spinbox)

        space_widget.setLayout(space_layout)
        self.main_layout.addWidget(space_widget)

        button_widget = QWidget(self)
        button_layout = QHBoxLayout()

        self.add_button = QPushButton('Add', button_widget)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.add_button.setFont(LABEL_FONT)
        button_layout.addWidget(self.add_button)
        button_widget.setLayout(button_layout)

        self.main_layout.addWidget(button_widget)

        self.setLayout(self.main_layout)
        self.main_layout.addStretch()

    def add_button_clicked(self):
        flight_number = self.input_flight_number_widget.get_input()
        country_from, admin1_from, admin2_from = self.select_origin_location_widget.get_selected_location()
        country_to, admin1_to, admin2_to = self.select_destination_location_widget.get_selected_location()
        departure_time = self.select_departure_time_widget.get_time()
        arrival_time = self.select_arrival_time_widget.get_time()
        economy_class_count, business_class_count, first_class_count = self.economy_class_spinbox.value(), self.business_class_spinbox.value(), self.first_class_spinbox.value()
        economy_class_price = 0
        business_class_price = 0
        first_class_price = 0
        if economy_class_count > 0:
            while True:
                economy_class_price, ok = QInputDialog.getDouble(None, "Input dialog", "Please set the unit price for economy class:", min=0)
                if ok:
                    break
        if business_class_count > 0:
            while True:
                business_class_price, ok = QInputDialog.getDouble(None, "Input dialog", "Please set the unit price for business class:", min=0)
                if ok:
                    break
        if first_class_count > 0:
            while True:
                first_class_price, ok = QInputDialog.getDouble(None, "Input dialog", "Please set the unit price for first class:", min=0)
                if ok:
                    break

        success, message = add_flight(flight_number, country_from, admin1_from, admin2_from, country_to, admin1_to, admin2_to, departure_time, arrival_time,
                                      economy_class_count, business_class_count, first_class_count,
                                      economy_class_price,business_class_price,first_class_price)
        if not success:
            QMessageBox.critical(self, 'Error', message)
        else:
            QMessageBox.information(self, 'Information', message)
