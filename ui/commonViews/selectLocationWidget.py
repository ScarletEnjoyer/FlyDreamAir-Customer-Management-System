from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from ui.constant import LABEL_FONT, countries
from object.country import Country


class SelectLocationWidget(QWidget):
    def __init__(self, parent, prompt: str):
        super().__init__(parent)
        layout = QHBoxLayout()

        self.prompt_label = QLabel(prompt, self)
        self.prompt_label.setFont(LABEL_FONT)
        layout.addWidget(self.prompt_label)

        self.country_combobox = QComboBox(self)

        self.country_combobox.setFixedWidth(150)
        self.country_combobox.setFont(LABEL_FONT)
        layout.addWidget(self.country_combobox)

        self.admin1_combobox = QComboBox(self)
        # self.admin1_combobox.setEditable(True)
        self.admin1_combobox.setFixedWidth(150)
        self.admin1_combobox.setFont(LABEL_FONT)
        layout.addWidget(self.admin1_combobox)

        self.admin2_combobox = QComboBox(self)
        # self.admin2_combobox.setEditable(True)
        self.admin2_combobox.setFixedWidth(150)
        self.admin2_combobox.setFont(LABEL_FONT)
        layout.addWidget(self.admin2_combobox)

        self.country_combobox.currentIndexChanged.connect(self.update_admin1)
        self.admin1_combobox.currentIndexChanged.connect(self.update_admin2)
        countries_names = countries.get_countries_names()
        self.country_combobox.addItems(countries_names)
        country_completer = QCompleter(countries_names, self.country_combobox)
        country_completer.setCaseSensitivity(False)
        country_completer.setFilterMode(Qt.MatchContains)
        self.country_combobox.setCompleter(country_completer)

        self.setLayout(layout)

    def update_admin1(self):
        self.admin1_combobox.clear()
        selected_country_name = self.country_combobox.currentText()
        country: Country = countries.get_country_by_name(selected_country_name)
        admin1_names = country.get_admin1_names()
        self.admin1_combobox.addItems(admin1_names)
        admin1_completer = QCompleter(admin1_names, self.admin1_combobox)
        admin1_completer.setCaseSensitivity(False)
        admin1_completer.setFilterMode(Qt.MatchContains)
        self.admin1_combobox.setCompleter(admin1_completer)

    def update_admin2(self):
        self.admin2_combobox.clear()
        selected_country_name = self.country_combobox.currentText()
        country: Country = countries.get_country_by_name(selected_country_name)
        selected_admin1_name = self.admin1_combobox.currentText()
        if selected_admin1_name == '':
            return
        admin1 = country.get_admin1_by_name(selected_admin1_name)
        admin2_names = admin1.get_next_level_divisions_names()
        self.admin2_combobox.addItems(admin2_names)
        admin2_completer = QCompleter(admin2_names, self.admin2_combobox)
        admin2_completer.setCaseSensitivity(False)
        admin2_completer.setFilterMode(Qt.MatchContains)
        self.admin1_combobox.setCompleter(admin2_completer)

    def get_selected_location(self):
        return self.country_combobox.currentText(), self.admin1_combobox.currentText(), self.admin2_combobox.currentText()

    def set_enabled(self,enabled):
        self.country_combobox.setEnabled(enabled)
        self.admin1_combobox.setEnabled(enabled)
        self.admin2_combobox.setEnabled(enabled)