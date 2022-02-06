import random
import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic

from Tools.genFont import genFont
from Tools.Image_Process import maskImage

try:
    from Interface.MainWindow import MainWindow
except:
    from MainWindow import MainWindow

from Engine import Engine


class MainBKG(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./Interface/MainBKG.ui", self)
        pixmap = maskImage("./src/mainbkgx.jpg", "jpg", 426, 200, 0)
        self.label_2.setPixmap(pixmap)

    def loadPixmap(self, label: QtWidgets.QLabel, data: bytes):
        image = QtGui.QImage()
        image.loadFromData(data)
        label.setPixmap(QtGui.QPixmap(image))
        label.setScaledContents(True)


class TextLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        genFont(painter, "Century Gothic", 22, QtCore.QPointF(
            40, 170), "Heading For Your Music...")
        painter.end()


class PaintLabel(QtWidgets.QLabel):
    _mainWindow: MainWindow
    _engine: Engine

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self._mainWindow = self.parent().parent().parent()
        except:
            self._mainWindow = None
        self._mainWindow.SearchStatusChanged.connect(self.update)
        self._mainWindow.ShowResult.connect(self.update)

    def setEngine(self, engine: Engine):
        self._engine = engine

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        self.colorDesign(painter)
        if self._mainWindow.status == 1:
            # flag = 0
            # if flag == 1:
            self.fontDesign(painter)
            self.parent().lineEdit.setVisible(True)
            self.parent().label_3.setVisible(False)
            self.parent().label_4.setVisible(False)
            self.parent().label_5.setVisible(False)
            self.parent().btnLeft.setVisible(False)
            self.parent().btnRight.setVisible(False)
        else:
            self.parent().lineEdit.setVisible(False)
            self.parent().label_3.setVisible(True)
            self.parent().label_4.setVisible(True)
            self.searchDesign(painter)
        painter.end()

    def btnDesign(self, painter: QtGui.QPainter) -> None:
        painter.setBrush(QtCore.Qt.GlobalColor.black)
        pathLeft = QtGui.QPainterPath()
        pathLeft.moveTo(400, 250)
        pathLeft.lineTo(400, 330)
        pathLeft.lineTo(420, 290)
        pathLeft.lineTo(400, 250)
        painter.drawPath(pathLeft)
        pathRight = QtGui.QPainterPath()
        pathRight.moveTo(25, 250)
        pathRight.lineTo(25, 330)
        pathRight.lineTo(5, 290)
        pathRight.lineTo(25, 250)
        painter.drawPath(pathRight)

    def fontDesign(self, painter: QtGui.QPainter) -> None:
        genFont(painter, "Century Gothic", 30,
                QtCore.QPointF(15, 70), "MusicBeta:", True)
        genFont(painter, "Century Gothic", 22,
                QtCore.QPointF(150, 120), "INS-2.0", True)
        genFont(painter, "./src/FontWel.ttf", 30,
                QtCore.QPointF(235, -150), "[Version]", type="file", color=QtGui.QColor("white"), rotate=40)
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
        painter.setBrush(QtGui.QColor("#2F94FD"))
        painter.drawEllipse(210, 250, 15, 15)
        painter.setPen(QtGui.QPen(QtGui.QColor("red"), 3))
        painter.drawLine(200, 248, 170, 230)
        painter.setPen(QtGui.QPen(QtGui.QColor("#FA7A33"), 3))
        painter.drawLine(240, 255, 260, 255)
        painter.setPen(QtGui.QPen(QtGui.QColor("white"), 3))
        painter.drawLine(216, 275, 216, 290)

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

    def searchDesign(self, painter: QtGui.QPainter) -> None:
        genFont(painter, "./src/FontWel.ttf", 30,
                QtCore.QPointF(235, -150), "[Search]", type="file", color=QtGui.QColor("white"), rotate=40)
        genFont(painter, "Century Gothic", 30,
                QtCore.QPointF(15, 70), "Result for:", True)
        genFont(painter, "Microsoft Yahei UI",
                20, QtCore.QPointF(15, 120), f"[{self._mainWindow.keyword}]", color=QtGui.QColor("white"))
        painter.setPen(QtGui.QPen(QtGui.QColor("white"), 2))
        painter.setBrush(QtCore.Qt.GlobalColor.transparent)
        if self._mainWindow.onSearch == False:
            painter.drawRoundedRect(75, 160, 280, 150, 15, 15)
            painter.drawRoundedRect(75, 330, 280, 150, 15, 15)
        if self._mainWindow.onShow == True:
            genFont(painter, "Century Gothic", 14, QtCore.QPointF(
                20, 490), f"{self._mainWindow.page}/{self._mainWindow.pages}")
            self.btnDesign(painter)
            item1 = self._engine._pipe.items[self._mainWindow.page * 2 - 2]
            item2 = self._engine._pipe.items[self._mainWindow.page * 2 - 1]
            self.parent().loadPixmap(self.parent().label_3, item1.imgData)
            self.parent().loadPixmap(self.parent().label_4, item2.imgData)
            genFont(painter, "Microsoft Yahei UI", 12, QtCore.QPointF(
                200, 200), f"{item1.song}", color=QtGui.QColor("red"))
            genFont(painter, "Microsoft Yahei UI", 12,
                    QtCore.QPointF(200, 230), f"{item1.singer}")
            genFont(painter, "Microsoft Yahei UI", 12, QtCore.QPointF(
                200, 370), f"{item2.song}", color=QtGui.QColor("red"))
            genFont(painter, "Microsoft Yahei UI", 12,
                    QtCore.QPointF(200, 400), f"{item2.singer}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainBKG()
    win.show()
    app.exec()
