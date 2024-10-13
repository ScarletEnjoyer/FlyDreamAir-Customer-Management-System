from PyQt5.QtGui import QFont
from object.countries import Countries
from tools.readCountryInfo import readCountryInfo
LABEL_FONT = QFont('SimSun', 12)

countries: Countries = readCountryInfo()
