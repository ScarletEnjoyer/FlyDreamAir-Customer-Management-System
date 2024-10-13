from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT


class InputFlightNumberWidget(QWidget):
    def __init__(self, parent, prompt: str,placeholder):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.prompt_label = QLabel(prompt, self)
        self.prompt_label.setFont(LABEL_FONT)
        layout.addWidget(self.prompt_label)

        self.line_edit = QLineEdit(self)
        self.line_edit.setFont(LABEL_FONT)
        self.line_edit.setPlaceholderText(placeholder)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def get_input(self):
        return self.line_edit.text()