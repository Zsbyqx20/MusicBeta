import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from Tools.genFont import genFont


class UserInfo(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./UserInfo.ui", self)
        # self.labelPic(self.label_5, "./src/regi.png")
        # self.labelPic(self.label_2, "./src/markgirl.png")

    def labelPic(self, label: QtWidgets.QLabel, src: str) -> None:
        label.setPixmap(QtGui.QPixmap(src))
        label.setScaledContents(True)


class TextLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        genFont(painter, "Century Gothic", 14,
                QtCore.QPointF(20, 79), "User:", True)
        genFont(painter, "Century Gothic", 12,
                QtCore.QPointF(50, 114), "Status:", True)
        genFont(painter, "Century Gothic", 12, QtCore.QPointF(
            102, 114), "Registered!", True, color=QtGui.QColor("#99CC66"))
        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = UserInfo()
    win.show()
    app.exec()
