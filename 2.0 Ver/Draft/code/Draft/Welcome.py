import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic

from Tools.genFont import genFont


class Welcome_Widget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./Welcome_Widget.ui", self)
        self.label_1.setPixmap(QtGui.QPixmap('./src/woman.png'))
        self.label_1.setScaledContents(True)
        self.label_4.setPixmap(QtGui.QPixmap('./src/man.png'))
        self.label_4.setScaledContents(True)
        self.putShadows(self.label_5)

    def putShadows(self, label: QtWidgets.QLabel) -> None:
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0.5)
        shadow.setColor(QtGui.QColor("#ffc6cb"))
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        label.setGraphicsEffect(shadow)


class TextLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.linkText = {
            "label_3": "MusicBeta 2.0 Version",
            "label_2": "2022, Stay with U..."
        }

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        color = QtGui.QLinearGradient(0, 0, self.width(), 0)
        color.setSpread(QtGui.QGradient.Spread.ReflectSpread)
        color.setColorAt(0, QtGui.QColor("#C051FF"))
        color.setColorAt(1, QtGui.QColor("#FF5A00"))
        genFont(painter, "./src/FontChi.ttf", 22, QtCore.QPointF(2, 25),
                self.linkText[self.objectName()], type="file", color=color)
        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Welcome_Widget()
    win.show()
    app.exec()
