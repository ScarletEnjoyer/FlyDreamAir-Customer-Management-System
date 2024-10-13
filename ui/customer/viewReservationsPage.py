from PyQt5.QtWidgets import *
from ui.customer.reservationItemWidget import ReservationItemWidget
from api.reservationApi import get_reservations_by_username


class ViewReservationsPage(QScrollArea):
    def __init__(self, customer_main_page, customer):
        super().__init__(customer_main_page)
        self.customer = customer
        self.setWidgetResizable(True)
        self.scroll_content = QWidget(self)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_content.setLayout(self.scroll_layout)
        reservations = get_reservations_by_username(self.customer.username)
        for i in range(len(reservations)):
            item_widget = ReservationItemWidget(self.scroll_content, i, reservations[i])
            item_widget.cancel_signal.connect(self.update_list)
            self.scroll_layout.addWidget(item_widget)
        self.scroll_content.setMinimumHeight(200 * len(reservations))
        self.scroll_layout.addStretch()
        self.setWidget(self.scroll_content)

    def update_list(self):
        reservations = get_reservations_by_username(self.customer.username)
        while self.scroll_layout.count() > 0:
            item = self.scroll_layout.takeAt(self.scroll_layout.count() - 1)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        for i in range(len(reservations)):
            item_widget = ReservationItemWidget(self.scroll_content, i, reservations[i])
            item_widget.cancel_signal.connect(self.update_list)
            self.scroll_layout.addWidget(item_widget)
        self.scroll_content.setMinimumHeight(200 * len(reservations))
        self.scroll_layout.addStretch()