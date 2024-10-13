from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from ui.admin.flightItemWidget import FlightItemWidget
from api.flightApi import get_flights


class ViewFlightsPage(QScrollArea):
    def __init__(self, admin_main_page):
        super().__init__(admin_main_page)
        # self.setObjectName('scroll_area')
        # self.setStyleSheet('QScrollArea#scroll_area {background-color: orange;}')
        self.setWidgetResizable(True)
        self.scroll_content = QWidget(self)
        # self.scroll_content.setFixedHeight(500)
        # self.scroll_content.setObjectName('scroll_content')
        # self.scroll_content.setStyleSheet('QWidget#scroll_content {background-color: white;}')
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_content.setLayout(self.scroll_layout)
        flights = get_flights()
        for i in range(len(flights)):
            item_widget=FlightItemWidget(self.scroll_content, i, flights[i])
            item_widget.remove_signal.connect(self.update_list)
            self.scroll_layout.addWidget(item_widget)
        self.scroll_content.setMinimumHeight(200 * len(flights))
        self.scroll_layout.addStretch()
        self.setWidget(self.scroll_content)

    def update_list(self):
        while self.scroll_layout.count() > 0:
            item = self.scroll_layout.takeAt(self.scroll_layout.count() - 1)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        flights = get_flights()
        for i in range(len(flights)):
            item_widget = FlightItemWidget(self.scroll_content, i, flights[i])
            item_widget.remove_signal.connect(self.update_list)
            self.scroll_layout.addWidget(item_widget)
        self.scroll_content.setMinimumHeight(200 * len(flights))
        self.scroll_layout.addStretch()
