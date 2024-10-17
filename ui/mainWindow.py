from PyQt5.QtWidgets import *

from ui.registerPage import RegisterPage
from ui.loginPage import LoginPage
from ui.admin.adminMainPage import AdminMainPage
from ui.customer.customerMainPage import CustomerMainPage
from object.admin import Admin
from api.loginApi import is_admin


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FlyDreamAir Management')
        self.setGeometry(0, 0, 800, 600)
        self.setFixedSize(800, 600)
        self.move_to_center()
        self.setObjectName('main_window')
        self.setStyleSheet('QMainWindow#main_window{background-color:white}'
                           'QStackedWidget#main_stacked_widget {border-image: url(background.png); background-size: cover;}')
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setObjectName('main_stacked_widget')
        # self.stacked_widget.setStyleSheet(f"QStackedWidget {{background-image: url(22.png); background-size: cover;}}")
        self.setCentralWidget(self.stacked_widget)
        self.display_login_page()

    def move_to_center(self):
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def display_login_page(self):
        self.stacked_widget.removeWidget(self.stacked_widget.currentWidget())
        self.stacked_widget.addWidget(LoginPage(self))

    def display_Register_page(self):
        self.stacked_widget.removeWidget(self.stacked_widget.currentWidget())
        self.stacked_widget.addWidget(RegisterPage(self))

    def login(self, user):
        self.stacked_widget.removeWidget(self.stacked_widget.currentWidget())
        if is_admin(user):
            self.stacked_widget.addWidget(AdminMainPage(self))
        else:
            self.stacked_widget.addWidget(CustomerMainPage(self, user))
