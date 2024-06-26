# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TasknPDfGE.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QWidget)
import Calendar
import openaiApi
import Icons_rc
from datetime import datetime
from openaiApi.main import getEvent

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 31)
        Form.setStyleSheet(u"*{\n"
"background-color: rgb(55,65,81);\n"
"color: white;\n"
"}\n"
"spam{\n"
"margin-left:2px;\n"
"}")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 740, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMaximumSize(QSize(23, 16777215))
        self.horizontalLayout.addWidget(self.radioButton)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(91, 0))
        self.label.setStyleSheet(u"border-left:1px solid white;text-align:center;")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(420, 0))
        self.label_2.setStyleSheet(u"border-left:1px solid white;border-right:1px solid white;")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 16777215))
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border-left:1px solid white;border-right:1px solid white;")

        self.horizontalLayout.addWidget(self.label_4)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/Icons/Images/calendar_add_on_24dp_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.clicked.connect(self.addEvent)
        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radioButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Descripcion</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Fecha</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Hora</span></p></body></html>", None))
        self.pushButton.setText("")
    # retranslateUi
    def addEvent(self):
        summary = self.label.text()
        desc = self.label_2.text()
        dtstart = self.label_3.text().replace(' ','')
        dtend = self.label_4.text().replace(' ','')
        result = getEvent(summary+'.'+desc+'.'+dtstart+'.'+dtend)
        result = result.split('.')
        summary = result[0]
        startevent = datetime(int(result[1]),int(result[2]),int(result[3]),int(result[4]),int(result[5]))
        endevent = datetime(int(result[6]),int(result[7]),int(result[8]),int(result[9]),int(result[10]))
        Calendar.CreateEvent(summary,startevent,endevent)