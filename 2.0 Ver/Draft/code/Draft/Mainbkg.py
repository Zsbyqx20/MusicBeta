import random
import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from Tools.Image_Process import maskImage
from Tools.genFont import genFont


class MainBKG(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./MainBKG.ui", self)
        pixmap = maskImage("./src/mainbkgx.jpg", "jpg", 426, 200, 0)
        self.label_2.setPixmap(pixmap)


class PaintLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     qp = QtGui.QPainter()
    #     qp.begin(self)
    #     pen = QtGui.QPen(QtGui.QColor("#FF6D0C"), 2)
    #     qp.setPen(pen)
    #     # self.getPoint(0, 33, 65, 265, 20, qp)
    #     # self.getPoint(0, 425, 50, 80, 35, qp)
    #     # self.getPoint(392, 425, 65, 265, 20, qp)
    #     qp.end()
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        self.colorDesign(painter)
        # painter.rotate(-30)
        self.fontDesign(painter)
        painter.setBrush(QtGui.QColor("#2F94FD"))
        painter.drawEllipse(210, 250, 15, 15)
        painter.setPen(QtGui.QPen(QtGui.QColor("red"), 3))
        painter.drawLine(200, 248, 170, 230)
        painter.setPen(QtGui.QPen(QtGui.QColor("#FA7A33"), 3))
        painter.drawLine(240, 255, 260, 255)
        painter.setPen(QtGui.QPen(QtGui.QColor("white"), 3))
        painter.drawLine(216, 275, 216, 290)
        painter.end()

    def fontDesign(self, painter: QtGui.QPainter) -> None:
        genFont(painter, "Century Gothic", 30,
                QtCore.QPointF(15, 70), "MusicBeta:", True)
        genFont(painter, "Century Gothic", 22,
                QtCore.QPointF(150, 120), "INS-2.0", True)
        genFont(painter, "./src/FontWel.ttf", 30,
                QtCore.QPointF(235, -150), "Version", type="file", color=QtGui.QColor("white"), rotate=40)
        genFont(painter, "Century Gothic", 16,
                QtCore.QPointF(10, 260), "\" Purify Your", True)    
        genFont(painter, "Century Gothic", 28,
                QtCore.QPointF(70, 220), "SOUL", True, color=QtGui.QColor("red")) 
        genFont(painter, "Century Gothic", 16,
                QtCore.QPointF(210, 210), "by getting", True)
        genFont(painter, "Century Gothic", 28,
                QtCore.QPointF(270, 260), "CLOSER", True, color=QtGui.QColor("#FC7C34")) 
        genFont(painter, "Century Gothic", 20,
                QtCore.QPointF(140, 320), "to Music. \"", True, color=QtGui.QColor("white"))
        genFont(painter, "Century Gothic", 16,
                QtCore.QPointF(115, 480), "Start Your Tour Here...", True)

    def colorDesign(self, painter: QtGui.QPainter) -> None:
        path = QtGui.QPainterPath()
        path.moveTo(129, 0)
        path.cubicTo(351, 29.6, 129, 148, 425, 148)
        path.lineTo(425, 0)
        path.lineTo(129, 0)
        color = QtGui.QLinearGradient(0, 0, 0, 250)
        color.setColorAt(0, QtGui.QColor("#878299"))
        color.setColorAt(1, QtGui.QColor("#A0A1B3"))
        painter.setBrush(color)
        painter.setPen(QtCore.Qt.GlobalColor.transparent)
        painter.drawPath(path)

    def getPoint(self, x1: int, x2: int, y1: int, y2: int, num: int, qp: QtGui.QPainter) -> None:
        for _ in range(num):
            x = random.randint(x1, x2)
            y = random.randint(y1, y2)
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainBKG()
    win.show()
    app.exec()
