# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GptgODZTN.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QTextEdit, QWidget)
import Icons_rc

class Ui_Dialog(object):
    """Gpt Dialog Class

    Args:
        object (QDialog): Class to Generate a Task with a GPT API inplementation.
    """
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(455, 186)
        Dialog.setMaximumSize(QSize(455, 186))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/Images/TaskFlowApp.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"*{\n"
"background-color: rgb(31, 41, 55);color: white;font: 10pt \"Consolas\";\n"
"}\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 70, 26))
        self.label.setStyleSheet(u"color: darkcyan;border: 2px solid #ccc;border-radius:4px;padding:2px;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 10, 11, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 10, 41, 31))
        self.label_3.setStyleSheet(u"border-image: url(:/Icons/Images/GPT.png);")
        self.label_gpt = QLabel(Dialog)
        self.label_gpt.setObjectName(u"label_gpt")
        self.label_gpt.setGeometry(QRect(20, 50, 411, 21))
        self.label_gpt.setStyleSheet(u"")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 80, 411, 61))
        self.textEdit.setStyleSheet(u"border:none;")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(260, 150, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"TaskFlow+GPT", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">TaskFlow</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">+</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_gpt.setText(QCoreApplication.translate("Dialog", u">GPT: ", None))
    # retranslateUi

