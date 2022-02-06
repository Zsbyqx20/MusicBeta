import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic

from Tools.genFont import genFont


class Contributor(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./Contributor.ui", self)
        self.putShadows(self.label_1)
        self.labelPic(self.label_3, "./src/result.png")
        self.labelPic(self.label_5, "./src/arty.png")

    def putShadows(self, label: QtWidgets.QLabel) -> None:
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0.5)
        shadow.setColor(QtGui.QColor("#ffc6cb"))
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        label.setGraphicsEffect(shadow)

    def labelPic(self, label: QtWidgets.QLabel, src: str) -> None:
        label.setPixmap(QtGui.QPixmap(src))
        label.setScaledContents(True)


class PaintLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        color = QtGui.QLinearGradient(0, 0, 120, 0)
        color.setColorAt(0, QtGui.QColor("#FF345F"))
        color.setColorAt(1, QtGui.QColor("#FFB400"))
        genFont(painter, "Century Gothic", 16,
                QtCore.QPointF(65, 50), "Contributor", True)
        genFont(painter, "Century Gothic", 16, 
                QtCore.QPointF(10, 99), "Zsbyqx2020", True, color)
        genFont(painter, "Century Gothic", 12,
                QtCore.QPointF(10, 127), "The one who loves", True)
        genFont(painter, "Century Gothic", 12,
                QtCore.QPointF(10, 147), "CREATING...", True)
        pen = QtGui.QPen(QtCore.Qt.GlobalColor.black, 2)
        pen.setStyle(QtCore.Qt.PenStyle.DotLine)
        painter.setPen(pen)
        painter.drawLine(65, 62, 185, 62)
        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Contributor()
    win.show()
    app.exec()
