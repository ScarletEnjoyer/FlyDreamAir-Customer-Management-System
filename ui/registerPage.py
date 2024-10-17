from PyQt5.QtWidgets import *
from ui.constant import *
from api.registerApi import register


class RegisterPage(QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.content_widget = QWidget(self)
        self.content_widget.setGeometry(250, 150, 300, 100)
        self.layout = QGridLayout(self.content_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.username_label = QLabel('Username:', self.content_widget)
        self.username_label.setFont(LABEL_FONT)
        self.layout.addWidget(self.username_label, 0, 0)

        self.username_input = QLineEdit(self.content_widget)
        self.username_input.setFont(LABEL_FONT)
        self.layout.addWidget(self.username_input, 0, 1)

        self.password_label = QLabel('Password:', self.content_widget)
        self.password_label.setFont(LABEL_FONT)
        self.layout.addWidget(self.password_label, 1, 0)

        self.password_input = QLineEdit(self.content_widget)
        self.password_input.setFont(LABEL_FONT)
        # self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input, 1, 1)

        self.password_confirm_label = QLabel('Confirm:', self.content_widget)
        self.password_confirm_label.setFont(LABEL_FONT)
        self.layout.addWidget(self.password_confirm_label, 2, 0)

        self.password_confirm_input = QLineEdit(self.content_widget)
        self.password_confirm_input.setFont(LABEL_FONT)
        # self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_confirm_input, 2, 1)

        self.register_button = QPushButton('Register', self)
        self.register_button.setFont(LABEL_FONT)
        self.register_button.setGeometry(250, 270, 100, 25)
        self.register_button.clicked.connect(self.on_register_clicked)

        self.return_button = QPushButton('Return', self)
        self.return_button.setFont(LABEL_FONT)
        self.return_button.setGeometry(450, 270, 100, 25)
        self.return_button.clicked.connect(self.on_return_clicked)

        self.status_label = QLabel('', self)
        self.status_label.setStyleSheet('color: red;')
        self.status_label.setFont(LABEL_FONT)
        self.status_label.setGeometry(250, 300, 400, 25)

    def on_register_clicked(self):
        self.status_label.setText('')
        username = self.username_input.text()
        password = self.password_input.text()
        confirm = self.password_confirm_input.text()
        success, message = register(username, password, confirm)
        if success:
            self.status_label.setStyleSheet('color: green;')
        else:
            self.status_label.setStyleSheet('color: red;')
        self.status_label.setText(message)

    def on_return_clicked(self):
        self.main_window.display_login_page()
