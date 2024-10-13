from PyQt5.QtWidgets import *


class MultiSelectDialog(QDialog):
    def __init__(self, parent,options):
        super().__init__(parent)
        self.setWindowTitle("多选对话框")

        self.layout = QVBoxLayout(self)

        self.checkboxes = []
        for option in options:
            checkbox = QCheckBox(option)
            self.layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_selected_options(self):
        return [cb.text() for cb in self.checkboxes if cb.isChecked()]