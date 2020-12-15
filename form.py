# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2 import QtGui
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Ui_gui(object):
    def setupUi(self, gui):
        if not gui.objectName():
            gui.setObjectName(u"Neural")
        gui.resize(430, 450)
        self.pushButton_load = QPushButton(gui)
        self.pushButton_load.setObjectName(u"pushButton_load")
        self.pushButton_load.setGeometry(QRect(260, 40, 111, 41))
        self.pushButton_recognize = QPushButton(gui)
        self.pushButton_recognize.setObjectName(u"pushButton_recognize")
        self.pushButton_recognize.setGeometry(QRect(260, 180, 111, 61))
        self.frame = QFrame(gui)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 40, 200, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 200, 200))
        self.label.setScaledContents(True)
        self.label.setText("")

        self.textEdit_output = QTextEdit(gui)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setGeometry(QRect(40, 310, 341, 91))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_output.setFont(font)

        self.retranslateUi(gui)
        self.pushButton_load.clicked.connect(gui.load)
        self.pushButton_recognize.clicked.connect(gui.recognize)

        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def setpixmap(self, pixmap):
        self.label.setPixmap(pixmap)
        self.label.show()

    def setletter(self, letter):
        self.textEdit_output.setText(letter)

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"gui", None))
        self.pushButton_load.setText(QCoreApplication.translate("gui", u"Wczytaj...", None))
        self.pushButton_recognize.setText(QCoreApplication.translate("gui", u"Rozpoznaj", None))
        self.textEdit_output.setHtml(QCoreApplication.translate("Neural", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi
