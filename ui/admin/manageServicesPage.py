from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT
from api.serviceApi import add_service
from api.serviceApi import get_services


class ManageServicesPage(QWidget):
    def __init__(self, admin_main_page):
        super().__init__(admin_main_page)
        self.main_layout = QVBoxLayout()
        self.top_widget = QWidget(self)
        self.top_layout = QHBoxLayout()

        self.name_label = QLabel('Service name:', self.top_widget)
        self.name_label.setFont(LABEL_FONT)
        self.top_layout.addWidget(self.name_label)

        self.name_lineedit = QLineEdit(self.top_widget)
        self.top_layout.addWidget(self.name_lineedit)

        self.unit_price_label = QLabel('Unit price:', self.top_widget)
        self.unit_price_label.setFont(LABEL_FONT)
        self.top_layout.addWidget(self.unit_price_label)

        self.unit_price_spinbox = QDoubleSpinBox(self.top_widget)
        self.unit_price_spinbox.setFont(LABEL_FONT)
        self.top_layout.addWidget(self.unit_price_spinbox)

        self.add_button = QPushButton('Add', self.top_widget)
        self.add_button.setFont(LABEL_FONT)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.top_layout.addWidget(self.add_button)

        self.top_widget.setLayout(self.top_layout)
        self.main_layout.addWidget(self.top_widget)
        self.model = None
        self.table_view = QTableView(self)
        self.table_view.setFont(LABEL_FONT)
        self.table_view.horizontalHeader().setFont(LABEL_FONT)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.main_layout.addWidget(self.table_view)
        self.update_table_view()
        self.setLayout(self.main_layout)

    def add_button_clicked(self):
        service_name = self.name_lineedit.text()
        unit_price = self.unit_price_spinbox.value()
        success, message = add_service(service_name, unit_price)
        if not success:
            QMessageBox.critical(self, 'Error', message)
        else:
            QMessageBox.information(self, 'Information', message)
            self.update_table_view()

    def update_table_view(self):
        services = get_services()
        self.model = QStandardItemModel(len(services), 2)
        self.model.setHorizontalHeaderLabels(['Service name', 'Unit price'])
        for i, service in enumerate(services):
            self.model.setItem(i, 0, QStandardItem(service.name))
            self.model.setItem(i, 1, QStandardItem(str(service.unit_price)))
        self.table_view.setModel(self.model)
