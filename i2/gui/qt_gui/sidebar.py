from ui_gui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Recommender System")


        self.dashboard_2.clicked.connect(self.switch_to_page_1)

        self.profile_2.clicked.connect(self.switch_to_page_2)

        self.messages_2.clicked.connect(self.switch_to_page_3)

        self.notifications_2.clicked.connect(self.switch_to_page_4)

        self.settings_2.clicked.connect(self.switch_to_page_5)





    def switch_to_page_1(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_page_2(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_page_3(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_page_4(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_page_5(self):
        self.stackedWidget.setCurrentIndex(4)
