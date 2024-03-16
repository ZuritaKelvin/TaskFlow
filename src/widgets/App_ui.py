# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 435)
        MainWindow.setMinimumSize(QSize(772, 435))
        MainWindow.setStyleSheet(u"*{\n"
"background-color: rgb(31, 41, 55);color: white;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 95, 34))
        self.label.setStyleSheet(u"color: darkcyan;border: 2px solid #ccc;border-radius:4px;padding:2px;")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 120, 711, 21))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 80, 671, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setStyleSheet(u"border-left:1px solid white;")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(420, 0))
        self.label_3.setStyleSheet(u"border-left:1px solid white;border-right:1px solid white;")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border-left:1px solid white;border-right:1px solid white;")

        self.horizontalLayout.addWidget(self.label_5)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 30, 71, 30))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	color: white;\n"
"	border: none;\n"
"	background: none;\n"
"	font-weight: bold;\n"
"	font-size: 12pt;\n"
"	padding: 4px 4px 4px 4px;\n"
"}\n"
"#pushButton:hover{\n"
"	background-color:darkcyan;\n"
"	color: white;\n"
"	border: 2px solid darkcyan;\n"
"	border-radius: 4px;\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(550, 30, 71, 30))
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	color:white;\n"
"	border: none;\n"
"	background: none;\n"
"	font-weight: bold;\n"
"	font-size: 12pt;\n"
"	padding: 4px 4px 4px 4px;\n"
"}\n"
"#pushButton_2:hover{\n"
"	background-color:darkcyan;\n"
"	color: white;\n"
"	border: 2px solid darkcyan;\n"
"	border-radius: 4px;\n"
"}\n"
"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 30, 71, 30))
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"	color:red;\n"
"	border: none;\n"
"	background: none;\n"
"	font-weight: bold;\n"
"	font-size: 12pt;\n"
"	padding: 4px 4px 4px 4px;\n"
"}\n"
"#pushButton_3:hover{\n"
"	background-color:darkcyan;\n"
"	color: white;\n"
"	border: 2px solid darkcyan;\n"
"	border-radius: 4px;\n"
"}\n"
"")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 40, 241, 16))
        self.label_6.setStyleSheet(u"color:red;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TaskFlow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">TaskFlow</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Nombre</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Descripcion</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Fecha</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Hora</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_6.setText("")
    # retranslateUi

