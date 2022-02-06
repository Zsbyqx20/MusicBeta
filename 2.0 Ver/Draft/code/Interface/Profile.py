from PyQt6 import QtWidgets, uic, QtGui, QtCore
from Tools.Image_Process import maskImage
import sys


class Profile_Image(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.colors = [(QtGui.QColor("#6906FF"), QtGui.QColor("#07FFD9")),
                       (QtGui.QColor("#FF5F90"), QtGui.QColor("#FFF000"))]
        uic.loadUi("./Interface/Profile_Image.ui", self)
        self.label.setPixmap(QtGui.QPixmap("./src/result.png"))
        self.label.setScaledContents(True)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        w = 108
        radius = 49.5
        qp = QtGui.QPainter()
        target = QtGui.QLinearGradient(0, 0, w, w)
        target.setColorAt(0, self.colors[1][0])
        target.setColorAt(1, self.colors[1][1])
        pen = QtGui.QPen(target, 8, QtCore.Qt.PenStyle.SolidLine)
        qp.begin(self)
        qp.setPen(pen)
        qp.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        qp.drawEllipse(QtCore.QPointF(54.5, 54.5), radius, radius)
        qp.end()

class Profile_Bkg(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        uic.loadUi("./Interface/Profile_Bkg.ui", self)
        pixmap = maskImage("./src/mainbg3.jpg", "jpg", 200, 200, 450, type=1)
        self.label.setPixmap(pixmap)
    
    def labelPic(self, label: QtWidgets.QLabel, src: str) -> None:
        label.setPixmap(QtGui.QPixmap(src))
        label.setScaledContents(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Profile_Bkg()
    win.show()
    app.exec()
