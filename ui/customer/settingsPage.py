from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT
from api.customerApi import change_password


class SettingsPage(QWidget):
    def __init__(self, customer_main_page, customer):
        super().__init__(customer_main_page)
        self.customer = customer
        layout = QVBoxLayout()
        self.button = QPushButton('Change password', self)
        self.button.clicked.connect(self.button_clicked)
        self.button.setFont(LABEL_FONT)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def button_clicked(self):
        new_password, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter a new password:')
        if not ok:
            return
        change_password(self.customer.username, new_password)
        self.customer.password = new_password
        QMessageBox.information(self, 'Information', 'Password changed successfully!')
