from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT
from ui.commonViews.inputFlightNumberWidget import InputFlightNumberWidget
from ui.commonViews.selectLocationWidget import SelectLocationWidget
from ui.customer.flightItemWidget import FlightItemWidget
from api.flightApi import get_flights


class BookFlightPage(QWidget):
    def __init__(self, customer_main_page, customer):
        super().__init__(customer_main_page)
        self.customer = customer
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.search_widget = QWidget(self)
        self.search_layout = QVBoxLayout()
        self.search_layout.setContentsMargins(0, 0, 0, 0)
        self.input_flight_number_widget = InputFlightNumberWidget(self.search_widget, "Flight number:", "Partial or complete flight number. e.g. AA, 123 or AA123")
        self.search_layout.addWidget(self.input_flight_number_widget)

        self.line_2 = QWidget(self.search_widget)
        self.line_2_layout = QHBoxLayout()
        self.line_2_layout.setContentsMargins(0, 0, 0, 0)

        self.select_origin_location_widget = SelectLocationWidget(self.line_2, 'From:')
        self.select_origin_location_widget.set_enabled(False)
        self.line_2_layout.addWidget(self.select_origin_location_widget)
        self.select_original_location_checkbox = QCheckBox('Enable', self.line_2)
        self.select_original_location_checkbox.setFont(LABEL_FONT)
        self.select_original_location_checkbox.stateChanged.connect(self.select_original_location_checkbox_clicked)
        self.line_2_layout.addWidget(self.select_original_location_checkbox)
        self.line_2.setLayout(self.line_2_layout)
        self.search_layout.addWidget(self.line_2)

        self.line_3 = QWidget(self.search_widget)
        self.line_3_layout = QHBoxLayout()

        self.line_3_layout.setContentsMargins(0, 0, 0, 0)

        self.select_destination_location_widget = SelectLocationWidget(self.line_3, 'To:')
        self.select_destination_location_widget.set_enabled(False)
        self.line_3_layout.addWidget(self.select_destination_location_widget)
        self.select_destination_location_checkbox = QCheckBox('Enable', self.line_3)
        self.select_destination_location_checkbox.setFont(LABEL_FONT)
        self.select_destination_location_checkbox.stateChanged.connect(self.select_destination_location_checkbox_clicked)
        self.line_3_layout.addWidget(self.select_destination_location_checkbox)
        self.line_3.setLayout(self.line_3_layout)
        self.search_layout.addWidget(self.line_3)

        self.search_button = QPushButton('Search', self.search_widget)
        self.search_button.setMaximumWidth(100)
        self.search_button.setFont(LABEL_FONT)
        self.search_button.clicked.connect(self.search_button_clicked)
        self.search_layout.addWidget(self.search_button)

        self.search_widget.setLayout(self.search_layout)

        self.main_layout.addWidget(self.search_widget)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_content.setLayout(self.scroll_layout)

        flights = get_flights()
        for i in range(len(flights)):
            item_widget = FlightItemWidget(self.scroll_content, i, flights[i], self.customer)
            item_widget.update_signal.connect(self.update_list)
            self.scroll_layout.addWidget(item_widget)
        self.scroll_content.setMinimumHeight(200 * len(flights))
        self.scroll_layout.addStretch()
        self.scroll_area.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll_area)

        # self.main_layout.addStretch()
        self.setLayout(self.main_layout)

    def select_original_location_checkbox_clicked(self, state):
        if state == 2:
            self.select_origin_location_widget.set_enabled(True)
        else:
            self.select_origin_location_widget.set_enabled(False)

    def select_destination_location_checkbox_clicked(self, state):
        if state == 2:
            self.select_destination_location_widget.set_enabled(True)
        else:
            self.select_destination_location_widget.set_enabled(False)

    def search_button_clicked(self):
        self.update_list()

    def update_list(self):
        flights = get_flights()
        displayed_flights = []
        for flight in flights:
            if self.input_flight_number_widget.get_input() not in flight.flight_number:
                continue
            if self.select_original_location_checkbox.isChecked():
                country_from, admin1_from, admin2_from = self.select_origin_location_widget.get_selected_location()
                if flight.country_from != country_from or flight.admin1_from != admin1_from or flight.admin2_from != admin2_from:
                    continue
            if self.select_destination_location_checkbox.isChecked():
                country_to, admin1_to, admin2_to = self.select_origin_location_widget.get_selected_location()
                if flight.country_to != country_to or flight.admin1_to != admin1_to or flight.admin2_to != admin2_to:
                    continue
            displayed_flights.append(flight)
        while self.scroll_layout.count() > 0:
            item = self.scroll_layout.takeAt(self.scroll_layout.count() - 1)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        for i in range(len(displayed_flights)):
            item_widget = FlightItemWidget(self.scroll_content, i, flights[i], self.customer)
            item_widget.update_signal.connect(self.update_list)
            self.scroll_layout.addWidget(item_widget)
        self.scroll_content.setMinimumHeight(200 * len(flights))
        self.scroll_layout.addStretch()
