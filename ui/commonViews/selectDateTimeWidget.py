from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime
from ui.constant import LABEL_FONT


class SelectDateTimeWidget(QWidget):
    def __init__(self, parent, prompt: str):
        super().__init__(parent)
        layout = QHBoxLayout()

        self.prompt_label = QLabel(prompt, self)
        self.prompt_label.setFont(LABEL_FONT)
        layout.addWidget(self.prompt_label)
        # layout.addWidget(self.prompt_label)

        self.datetime_edit = QDateTimeEdit(self)
        self.datetime_edit.setFont(LABEL_FONT)
        self.datetime_edit.setFixedWidth(150)
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime_edit)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        # layout.addStretch()
        self.setLayout(layout)

    def get_time(self):
        return self.datetime_edit.dateTime()