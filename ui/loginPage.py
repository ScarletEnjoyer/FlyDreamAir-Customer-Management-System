from PyQt5.QtWidgets import *
from ui.constant import *
from api.loginApi import login


class LoginPage(QWidget):
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
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input, 1, 1)

        self.user_type_label = QLabel('Login as:', self.content_widget)
        self.user_type_label.setFont(LABEL_FONT)
        self.layout.addWidget(self.user_type_label, 2, 0)

        self.user_type_comboBox = QComboBox(self.content_widget)
        self.user_type_comboBox.addItem('Admin')
        self.user_type_comboBox.addItem('Customer')
        self.user_type_comboBox.setFont(LABEL_FONT)
        self.layout.addWidget(self.user_type_comboBox, 2, 1)

        self.login_button = QPushButton('Login', self)
        self.login_button.setFont(LABEL_FONT)
        self.login_button.setGeometry(250, 270, 100, 25)
        self.login_button.clicked.connect(self.on_login_clicked)

        self.register_button = QPushButton('Register', self)
        self.register_button.setFont(LABEL_FONT)
        self.register_button.setGeometry(450, 270, 100, 25)
        self.register_button.clicked.connect(self.on_register_clicked)

        self.status_label = QLabel('', self)
        self.status_label.setStyleSheet('color: red;')
        self.status_label.setFont(LABEL_FONT)
        self.status_label.setGeometry(250, 300, 300, 25)

        

    def on_register_clicked(self):
        self.main_window.display_Register_page()

    def on_login_clicked(self):
        self.status_label.setText('')
        username = self.username_input.text()
        password = self.password_input.text()
        user_type = self.user_type_comboBox.currentText()
        user, message = login(username, password, user_type)
        if user is None:
            self.status_label.setText(message)
        else:
            self.main_window.login(user)