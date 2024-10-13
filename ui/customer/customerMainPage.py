from PyQt5.QtWidgets import *
from ui.navigationBar import NavigationBar
from ui.customer.settingsPage import SettingsPage
from ui.customer.viewReservationsPage import ViewReservationsPage
from ui.customer.bookFlightPage import BookFlightPage


class CustomerMainPage(QWidget):
    def __init__(self, main_window, customer):
        super().__init__(main_window)
        self.main_window = main_window
        self.customer = customer
        self.setObjectName('customer_main_page')
        self.setStyleSheet('QWidget#customer_main_page {background-color: white;}')
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.options = ['My Reservations', 'Book flight', 'Settings', 'Quit']
        self.navigation_bar = NavigationBar(self.options)

        line = QFrame(self)
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setLineWidth(1)

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setObjectName('customer_stacked_widget')
        self.stacked_widget.setStyleSheet('QWidget#customer_stacked_widget {background-color: white;}')
        self.navigation_bar.currentRowChanged.connect(self.display_page)

        self.display_page(0)

        self.main_layout.addWidget(self.navigation_bar)
        self.main_layout.addWidget(line)
        self.main_layout.addWidget(self.stacked_widget)

    def display_page(self, index):
        self.stacked_widget.removeWidget(self.stacked_widget.currentWidget())
        if self.options[index] == 'My Reservations':
            self.stacked_widget.addWidget(ViewReservationsPage(self,self.customer))
        elif self.options[index] == 'Book flight':
            self.stacked_widget.addWidget(BookFlightPage(self,self.customer))
        elif self.options[index] == 'Settings':
            self.stacked_widget.addWidget(SettingsPage(self,self.customer))
        else:
            self.main_window.display_login_page()
