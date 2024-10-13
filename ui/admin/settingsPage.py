from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT
from api.customerApi import clear_customers
from api.flightApi import clear_flights
from api.reservationApi import clear_reservations


class SettingsPage(QWidget):
    def __init__(self, admin_main_page):
        super().__init__(admin_main_page)
        layout = QVBoxLayout()
        self.button = QPushButton('Clear all data', self)
        self.button.clicked.connect(self.button_clicked)
        self.button.setFont(LABEL_FONT)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def button_clicked(self):
        reply = QMessageBox.question(self, '', "Are you sure you want to clear all flights,customers' registration information, and reservation information", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply != QMessageBox.Yes:
            return
        clear_customers()
        clear_flights()
        clear_reservations()
        QMessageBox.information(self, 'Information', 'Data cleared!')
