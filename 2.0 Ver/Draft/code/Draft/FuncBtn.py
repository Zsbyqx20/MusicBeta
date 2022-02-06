import sys
from telnetlib import SE

from PyQt6 import QtCore, QtGui, QtWidgets, uic

from Tools.genFont import genFont
from Tools.Image_Process import maskImage


class FuncBtn(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./FuncBtn.ui", self)
        self.labelPic(self.label_6, "./src/Home.png")
        self.labelPic(self.label_7, "./src/ProfileEdit.png")
        self.labelPic(self.label_8, "./src/ExitM.png")
        self.btnGroup = QtWidgets.QButtonGroup(self)
        self.btnGroup.addButton(self.pushButton_4)
        self.btnGroup.addButton(self.pushButton_5)
        self.pushButton_4.clicked.connect(self.update)
        self.pushButton_5.clicked.connect(self.update)
        self.pushButton_6.clicked.connect(self.update)

        self.labelPic(self.label_1, "./src/homepage.png")
        self.labelPic(self.label_2, "./src/profile.png")
        self.labelPic(self.label_3, "./src/exit.png")
        pixmap = maskImage("./src/mainbkgx.jpg", "jpg", 200, 300, 400, 3)
        self.label_5.setPixmap(pixmap)
        self.pushButton_1.clicked.connect(self.startanim)
        self.pushButton_2.clicked.connect(self.startanim)
        self.pushButton_3.clicked.connect(self.startanim)
        self.link = {
            "pushButton_1": 1,
            "pushButton_2": 2,
            "pushButton_3": 3
        }
        try:
            self.pushButton_6.clicked.connect(self.parent().parent().close)
            # print(self.parent())
        except:
            self.pushButton_6.clicked.connect(self.close)

    def labelPic(self, label: QtWidgets.QLabel, src: str) -> None:
        label.setPixmap(QtGui.QPixmap(src))
        label.setScaledContents(True)

    def startanim(self):
        self.label_4.signal_src = self.link[self.sender().objectName()]
        self.label_4.anim.stop()
        self.label_4.anim.start()


class PaintLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._radius = 0
        self._signal_src = 0
        self.anim = QtCore.QPropertyAnimation(self, b"radius", self)
        self.anim.setDuration(800)
        self.anim.setStartValue(15)
        self.anim.setEndValue(25)

    @QtCore.pyqtProperty(float)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r: float):
        self._radius = r

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        pen = QtGui.QPen(QtCore.Qt.GlobalColor.transparent)
        # painter.setPen(pen)
        center = QtCore.QPointF(170, 70 * self.signal_src - 40)
        color = QtGui.QRadialGradient(center, 25)
        color.setColorAt(0, QtGui.QColor("#FFB400"))
        color.setColorAt(1, QtGui.QColor(255, 179, 0, 100))
        brush = QtGui.QBrush(color)
        painter.setBrush(brush)
        painter.setPen(pen)
        if self.anim.state() == QtCore.QPropertyAnimation.State.Running:
            painter.drawEllipse(center, self._radius, self._radius)
        painter.end()
        self.update()

    @property
    def signal_src(self):
        return self._signal_src

    @signal_src.setter
    def signal_src(self, name: int):
        self._signal_src = name


class TextLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        # if self.parent()
        color1 = QtGui.QColor("grey")
        color2 = QtGui.QColor("grey")
        color3 = QtGui.QColor("grey")
        if self.parent().pushButton_4.underMouse() or self.parent().pushButton_4.isChecked():
            color1 = QtGui.QColor("#2F94FD")
        if self.parent().pushButton_5.underMouse() or self.parent().pushButton_5.isChecked():
            color2 = QtGui.QColor("#FC7C34")
        if self.parent().pushButton_6.underMouse() or self.parent().pushButton_6.isChecked():
            color3 = QtGui.QColor("red")
        genFont(painter, "./src/FontWel.ttf", 18, QtCore.QPointF(90,
                110), "HOME", True, color=color1, type="file")
        genFont(painter, "./src/FontWel.ttf", 18, QtCore.QPointF(
            90, 170), "PROFILE", True, color=color2, type="file")
        genFont(painter, "./src/FontWel.ttf", 18, QtCore.QPointF(
            90, 230), "EXIT", True, color=color3, type="file")
        painter.end()


class TextButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.linkText = {
            "pushButton_1": "Home Page",
            "pushButton_2": "Edit Profile",
            "pushButton_3": "Exit",
        }
        self.linkPoint = {
            "pushButton_1": QtCore.QPointF(14, 36),  # 34
            "pushButton_2": QtCore.QPointF(20, 36),  # 40
            "pushButton_3": QtCore.QPointF(48, 36)  # 68
        }

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        if QtWidgets.QWidget.underMouse(self):
            color = QtGui.QColor(255, 213, 215)
        else:
            color = QtGui.QLinearGradient(0, 0, self.width(), 0)
            color.setColorAt(0, QtGui.QColor(255, 213, 215))
            color.setColorAt(1, QtGui.QColor(255, 90, 0, 100))
        painter.setBrush(QtGui.QBrush(color))
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.transparent))
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 15, 15)
        genFont(painter, "Century Gothic", 12,
                self.linkPoint[self.objectName()],
                self.linkText[self.objectName()])
        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = FuncBtn()
    win.show()
    app.exec()
