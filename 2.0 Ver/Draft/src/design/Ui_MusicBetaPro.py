# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Desktop\VScode工作区\MusicBeta2.0\src\design\MusicBetaPro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MusicBetaPro(object):
    def setupUi(self, MusicBetaPro):
        MusicBetaPro.setObjectName("MusicBetaPro")
        MusicBetaPro.resize(750, 464)
        font = QtGui.QFont()
        font.setFamily("汉仪懒美美 W")
        font.setPointSize(10)
        MusicBetaPro.setFont(font)
        self.BGwidget = QtWidgets.QWidget(MusicBetaPro)
        self.BGwidget.setGeometry(QtCore.QRect(0, 0, 752, 464))
        self.BGwidget.setMinimumSize(QtCore.QSize(752, 464))
        self.BGwidget.setMaximumSize(QtCore.QSize(752, 464))
        font = QtGui.QFont()
        font.setFamily("汉仪懒美美 W")
        font.setPointSize(12)
        self.BGwidget.setFont(font)
        self.BGwidget.setStyleSheet("background-color: rgb(0, 4, 14);")
        self.BGwidget.setObjectName("BGwidget")
        self.widget = QtWidgets.QWidget(self.BGwidget)
        self.widget.setGeometry(QtCore.QRect(110, 0, 900, 600))
        font = QtGui.QFont()
        font.setFamily("汉仪懒美美 W")
        font.setPointSize(12)
        self.widget.setFont(font)
        self.widget.setStyleSheet("image: url(:/img/space.png);")
        self.widget.setObjectName("widget")

        self.retranslateUi(MusicBetaPro)
        QtCore.QMetaObject.connectSlotsByName(MusicBetaPro)

    def retranslateUi(self, MusicBetaPro):
        _translate = QtCore.QCoreApplication.translate
        MusicBetaPro.setWindowTitle(_translate("MusicBetaPro", "MusicBetaPro"))
import img_rc
