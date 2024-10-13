from PyQt5.QtWidgets import QListWidget
from ui.constant import *


class NavigationBar(QListWidget):
    def __init__(self, options):
        super().__init__()
        for i, option in enumerate(options):
            self.insertItem(i, option)
        self.setFont(LABEL_FONT)
        self.setFixedWidth(150)
        self.setStyleSheet('''
            QListWidget {
                background-color: white;
                border: None;
                outline: 0;
            }
            QListWidget::item {
                background-color: #f0f0f0;
                padding: 10px;
                margin: 2px;
                border-radius: 5px;
                font-size: 25px; /* 设置字体大小 */
            }
            QListWidget::item:hover {
                background-color: #cce7ff; /* 鼠标移上去的效果 */
            }
            QListWidget::item:selected {
                background-color: #0078d7; /* 点击后的效果 */
                color: white;
            }
            QListWidget::item:selected:hover {
                background-color: #005bb5; /* 点击后鼠标悬停的效果 */
            }
        ''')
        self.setCurrentRow(0)

