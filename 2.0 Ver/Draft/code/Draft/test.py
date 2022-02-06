from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from Tools.genFont import genFont

class WinMain(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(450, 450)
        # self.setStyleSheet("background-color:red;")
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.show()
    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        imgdata = open("./src/Cloud.png", "rb").read()
        image = QtGui.QImage.fromData(imgdata, "png")
        image.convertToFormat(QtGui.QImage.Format.Format_ARGB32)
        brush = QtGui.QBrush(image)
        painter.setBrush(brush)
        painter.drawRect(0, 0, 100, 100)
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = WinMain()
    app.exec()