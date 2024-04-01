# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormIfnYLi.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from datetime import date, datetime
import Icons_rc

class Ui_Form(object):
    """Form Class
    Args:
    object (QForm): Form class to Create and Update Tasks.
    """
    def setupUi(self, Form):

        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(388, 356)
        Form.setMinimumSize(QSize(388, 356))
        Form.setMaximumSize(QSize(388, 16777215))
        icon = QIcon()
        icon.addFile(u":/Icons/Images/TaskFlowApp.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(31, 41, 55);color: white;text-align: center;")
        self.today = date.today()
        self.ahora = datetime.now()
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 70, 26))
        self.label.setStyleSheet(u"color: darkcyan;border: 2px solid #ccc;border-radius:4px;padding:2px;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 60, 62, 22))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 110, 88, 22))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 210, 43, 22))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 210, 37, 22))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 60, 91, 21))
        self.lineEdit.setStyleSheet(u"	background-color:rgb(51, 65, 85);\n"
"	border-radius: 2px;\n"
"	text-decoration: none;\n"
"	border: 1px solid #ccc")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 280, 75, 24))
        self.pushButton.setStyleSheet(u"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color:rgb(0, 170, 127);\n"
"color: white;\n"
"border-radius:4px;")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 240, 71, 21))
        self.lineEdit_2.setStyleSheet(u"	background-color:rgb(51, 65, 85);\n"
"	border-radius: 2px;\n"
"	text-decoration: none;\n"
"	border: 1px solid #ccc")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 240, 41, 20))
        self.lineEdit_3.setStyleSheet(u"	background-color:rgb(51, 65, 85);\n"
"	border-radius: 2px;\n"
"	text-decoration: none;\n"
"	border: 1px solid #ccc")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 140, 241, 21))
        self.lineEdit_4.setStyleSheet(u"	background-color:rgb(51, 65, 85);\n"
"	border-radius: 2px;\n"
"	text-decoration: none;\n"
"	border: 1px solid #ccc")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 180, 125, 16))
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.pushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">TaskFlow</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Nombre</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Descripcion</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Fecha</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Hora</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"A\u00f1adir", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_2.setText(QCoreApplication.translate("Form", str(self.today), None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", str(self.ahora.strftime('%H:%M')), None))
        self.label_6.setText("")
    # retranslateUi

