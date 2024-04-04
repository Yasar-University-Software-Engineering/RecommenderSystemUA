# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QScrollBar, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc
# import grafikler_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1009, 681)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.widget = QWidget(self.dashboard_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 991, 61))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}")
        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(-20, 10, 796, 41))
        self.horizontalLayout = QHBoxLayout(self.header_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(308, 14, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(338, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.widget_2 = QWidget(self.profile_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 991, 61))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}")
        self.header_widget_2 = QWidget(self.widget_2)
        self.header_widget_2.setObjectName(u"header_widget_2")
        self.header_widget_2.setGeometry(QRect(40, 10, 671, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(156, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.header_widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(156, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.tableWidget = QTableWidget(self.profile_page)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 21):
            self.tableWidget.setRowCount(21)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 180, 721, 351))
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(51)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_5 = QLabel(self.profile_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 70, 731, 101))
        font2 = QFont()
        font2.setFamilies([u"Dubai"])
        font2.setPointSize(11)
        self.label_5.setFont(font2)
        self.label_5.setAcceptDrops(False)
        self.label_5.setLineWidth(1)
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(18)
        self.label_5.setIndent(-1)
        self.verticalScrollBar_2 = QScrollBar(self.profile_page)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setGeometry(QRect(740, 60, 17, 2511))
        self.verticalScrollBar_2.setOrientation(Qt.Vertical)
        self.stackedWidget.addWidget(self.profile_page)
        self.messages_page = QWidget()
        self.messages_page.setObjectName(u"messages_page")
        self.widget_3 = QWidget(self.messages_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 991, 61))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}")
        self.header_widget_3 = QWidget(self.widget_3)
        self.header_widget_3.setObjectName(u"header_widget_3")
        self.header_widget_3.setGeometry(QRect(50, 10, 621, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.header_widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(156, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.header_widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(156, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.tableWidget_2 = QTableWidget(self.messages_page)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFont(font1);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFont(font1);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFont(font1);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFont(font1);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        if (self.tableWidget_2.rowCount() < 21):
            self.tableWidget_2.setRowCount(21)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(20, __qtablewidgetitem49)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 180, 721, 351))
        self.tableWidget_2.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_2.setFrameShadow(QFrame.Sunken)
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(51)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.label_6 = QLabel(self.messages_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 70, 731, 101))
        self.label_6.setFont(font2)
        self.label_6.setAcceptDrops(False)
        self.label_6.setLineWidth(1)
        self.label_6.setMidLineWidth(0)
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(18)
        self.label_6.setIndent(-1)
        self.verticalScrollBar_3 = QScrollBar(self.messages_page)
        self.verticalScrollBar_3.setObjectName(u"verticalScrollBar_3")
        self.verticalScrollBar_3.setGeometry(QRect(740, 60, 17, 2511))
        self.verticalScrollBar_3.setOrientation(Qt.Vertical)
        self.stackedWidget.addWidget(self.messages_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.widget_4 = QWidget(self.notifications_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 991, 61))
        self.widget_4.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}")
        self.header_widget_4 = QWidget(self.widget_4)
        self.header_widget_4.setObjectName(u"header_widget_4")
        self.header_widget_4.setGeometry(QRect(80, 10, 530, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(156, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_9 = QLabel(self.header_widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer_8 = QSpacerItem(156, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.label_7 = QLabel(self.notifications_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 120, 731, 131))
        self.label_7.setFont(font2)
        self.label_7.setAcceptDrops(False)
        self.label_7.setLineWidth(1)
        self.label_7.setMidLineWidth(0)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(18)
        self.label_7.setIndent(-1)
        self.label_10 = QLabel(self.notifications_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 240, 721, 581))
        self.label_10.setMargin(16)
        self.label_11 = QLabel(self.notifications_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 890, 731, 81))
        self.label_11.setFont(font2)
        self.label_11.setAcceptDrops(False)
        self.label_11.setLineWidth(1)
        self.label_11.setMidLineWidth(0)
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setMargin(18)
        self.label_11.setIndent(-1)
        self.label_12 = QLabel(self.notifications_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 960, 741, 381))
        self.label_12.setMargin(23)
        self.label_13 = QLabel(self.notifications_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 1530, 721, 991))
        self.label_14 = QLabel(self.notifications_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 1420, 731, 101))
        self.label_14.setFont(font2)
        self.label_14.setAcceptDrops(False)
        self.label_14.setLineWidth(1)
        self.label_14.setMidLineWidth(0)
        self.label_14.setTextFormat(Qt.PlainText)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setMargin(18)
        self.label_14.setIndent(-1)
        self.verticalScrollBar = QScrollBar(self.notifications_page)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(740, 60, 16, 2351))
        self.verticalScrollBar.setMinimum(1)
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.label_21 = QLabel(self.notifications_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 70, 271, 41))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(False)
        self.label_21.setFont(font3)
        self.label_21.setMargin(36)
        self.label_22 = QLabel(self.notifications_page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 850, 601, 41))
        self.label_22.setFont(font3)
        self.label_22.setMargin(36)
        self.label_23 = QLabel(self.notifications_page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 1370, 601, 41))
        self.label_23.setFont(font3)
        self.label_23.setMargin(36)
        self.stackedWidget.addWidget(self.notifications_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.widget_5 = QWidget(self.settings_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 991, 61))
        self.widget_5.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}")
        self.header_widget_5 = QWidget(self.widget_5)
        self.header_widget_5.setObjectName(u"header_widget_5")
        self.header_widget_5.setGeometry(QRect(0, 10, 620, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.header_widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(268, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.label_15 = QLabel(self.header_widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_15)

        self.horizontalSpacer_10 = QSpacerItem(153, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.label_8 = QLabel(self.settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 130, 731, 101))
        self.label_8.setFont(font2)
        self.label_8.setAcceptDrops(False)
        self.label_8.setLineWidth(1)
        self.label_8.setMidLineWidth(0)
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(18)
        self.label_8.setIndent(-1)
        self.label_16 = QLabel(self.settings_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(-10, 80, 391, 41))
        self.label_16.setFont(font3)
        self.label_16.setMargin(36)
        self.label_17 = QLabel(self.settings_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 230, 731, 251))
        self.label_17.setMargin(8)
        self.label_18 = QLabel(self.settings_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 520, 391, 41))
        self.label_18.setFont(font3)
        self.label_18.setMargin(36)
        self.label_19 = QLabel(self.settings_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 570, 751, 51))
        self.label_19.setFont(font2)
        self.label_19.setAcceptDrops(False)
        self.label_19.setLineWidth(1)
        self.label_19.setMidLineWidth(0)
        self.label_19.setTextFormat(Qt.PlainText)
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setMargin(18)
        self.label_19.setIndent(-1)
        self.label_20 = QLabel(self.settings_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 610, 731, 281))
        self.label_20.setMargin(12)
        self.verticalScrollBar_4 = QScrollBar(self.settings_page)
        self.verticalScrollBar_4.setObjectName(u"verticalScrollBar_4")
        self.verticalScrollBar_4.setGeometry(QRect(740, 60, 17, 2511))
        self.verticalScrollBar_4.setOrientation(Qt.Vertical)
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 30, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        font5 = QFont()
        font5.setPointSize(11)
        self.dashboard_2.setFont(font5)
        icon = QIcon()
        icon.addFile(u":/newPrefix/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/newPrefix/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.profile_2 = QPushButton(self.icon_name_widget)
        self.profile_2.setObjectName(u"profile_2")
        self.profile_2.setFont(font5)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/newPrefix/profile.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_2.setIcon(icon1)
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_2)

        self.messages_2 = QPushButton(self.icon_name_widget)
        self.messages_2.setObjectName(u"messages_2")
        self.messages_2.setFont(font5)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/newPrefix/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.messages_2.setIcon(icon2)
        self.messages_2.setCheckable(True)
        self.messages_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.messages_2)

        self.notifications_2 = QPushButton(self.icon_name_widget)
        self.notifications_2.setObjectName(u"notifications_2")
        self.notifications_2.setFont(font5)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/newPrefix/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.notifications_2.setIcon(icon3)
        self.notifications_2.setCheckable(True)
        self.notifications_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.notifications_2)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setFont(font5)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/newPrefix/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_2.setIcon(icon4)
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 209, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_8 = QPushButton(self.icon_name_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_8.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"K-Means Clustering Algoritm Recommendations", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"User ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Recommendation #1 ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Recommendation #2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Recommendation #3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The recommendation results of the K-Means Clustering Algorithm are listed on the table below. The table is extracted from the results .CSV file which contains more information. The table serves to give a quick insight on the spot.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"KNN Algorithm Recommendations", None))
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"User ID", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Recommendation #1 ", None));
        ___qtablewidgetitem27 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Recommendation #2", None));
        ___qtablewidgetitem28 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Recommendation #3", None));
        ___qtablewidgetitem29 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem43 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem44 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem45 = self.tableWidget_2.verticalHeaderItem(16)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem46 = self.tableWidget_2.verticalHeaderItem(17)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem47 = self.tableWidget_2.verticalHeaderItem(18)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem48 = self.tableWidget_2.verticalHeaderItem(19)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem49 = self.tableWidget_2.verticalHeaderItem(20)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"The recommendation results of the KNN (K Nearest Neighbour) Algorithm are listed on the table below. The table is extracted from the results .CSV file which contains more information. The table serves to give a quick insight on the spot.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Algorithm Analytics", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"The Correlation Matrix for the K-Means Clustering Algortihm is shown below. The matrix visualizes how close of a relationship the engineered attributes have. Looking at the heatmap, we can see that there are some pairs of variables that have high correlations. These high correlations indicate that these variables move closely together, implying a degree of multicollinearity. ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/correlation_matrix (1).jpg\"/></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"The below graph allows us to visualize how much variance each additional principal component can explain, thereby helping the algorithm to pinpoint the optimal number of components to retain for the analysis.", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/CV_vs_NoC (1).jpg\"/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/avg_silhouette_scot_for_k (1).jpg\"/></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"The graphs below visualize the testing step for each K values and their respective Silhouette scores. Silhouette scores for each k value to determine the one with the highest score. This way the choice gives us clusters that are more evenly matched and well-defined, making our clustering solution stronger and more reliable. ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Correlation Matrix", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Cumulative Variance vs. Number of Components", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Silhouette Scores for each K values", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Dataset Analytics", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Graph shows the inliers and outliners in the dataset. An outlier is a data value that lies in the tail of the statistical distribution of a set of data values. An inlier is an erroneous data value which actually lies in the interior of a statistical distribution.", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Inliers & Outliers", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/inliners_and_outliners (1).jpg\"/></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Missing Values", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Graph shows the percentage of missing values in each column of the dataset.", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/percentage_of_missing_values (1).jpg\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Recommender System", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
        self.profile_2.setText(QCoreApplication.translate("MainWindow", u"Clustering Recommendations", None))
        self.messages_2.setText(QCoreApplication.translate("MainWindow", u"KNN Recommendations", None))
        self.notifications_2.setText(QCoreApplication.translate("MainWindow", u"Algorithm Analytics", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Dataset Analytics", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

