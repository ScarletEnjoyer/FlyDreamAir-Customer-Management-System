from PyQt5.QtWidgets import *
from ui.navigationBar import NavigationBar
from ui.admin.viewFlightsPage import ViewFlightsPage
from ui.admin.addFlightPage import AddFlightPage
from ui.admin.manageServicesPage import ManageServicesPage
from ui.admin.settingsPage import SettingsPage


class AdminMainPage(QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        # self.setObjectName('admin_main_page')
        # self.setStyleSheet('QWidget#admin_main_page {background-color: white;}')
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.options = ['View Flights', 'Add Flight', 'Manage Services', 'Settings', 'Quit']
        self.navigation_bar = NavigationBar(self.options)

        line = QFrame(self)
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setLineWidth(1)

        self.stacked_widget = QStackedWidget(self)
        # self.stacked_widget.setObjectName('admin_stacked_widget')
        # self.stacked_widget.setStyleSheet('QWidget#admin_stacked_widget {background-color: white;}')
        self.navigation_bar.currentRowChanged.connect(self.display_page)

        self.display_page(0)

        self.main_layout.addWidget(self.navigation_bar)
        self.main_layout.addWidget(line)
        self.main_layout.addWidget(self.stacked_widget)

    def display_page(self, index):
        self.stacked_widget.removeWidget(self.stacked_widget.currentWidget())
        if self.options[index] == 'View Flights':
            self.stacked_widget.addWidget(ViewFlightsPage(self))
        elif self.options[index] == 'Add Flight':
            self.stacked_widget.addWidget(AddFlightPage(self))
        elif self.options[index] == 'Manage Services':
            self.stacked_widget.addWidget(ManageServicesPage(self))
        elif self.options[index] == 'Settings':
            self.stacked_widget.addWidget(SettingsPage(self))
        else:
            self.main_window.display_login_page()
