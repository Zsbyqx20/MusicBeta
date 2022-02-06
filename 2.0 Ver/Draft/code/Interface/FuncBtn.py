import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic

from Interface.MainWindow import MainWindow
from Tools.genFont import genFont
from Tools.Image_Process import maskImage


class FuncBtn(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./Interface/FuncBtn.ui", self)
        try:
            self._mainWindow:MainWindow = self.parent().parent()
        except:
            self._mainWindow = None
        self._homeBtn: QtWidgets.QPushButton = self.pushButton_4
        self._searchBtn: QtWidgets.QPushButton = self.pushButton_5
        self._exitBtn: QtWidgets.QPushButton = self.pushButton_6

        self.labelPic(self.label_6, "./src/Home.png")
        self.labelPic(self.label_7, "./src/ProfileEdit.png")
        self.labelPic(self.label_8, "./src/Exit.png")

        self.btnGroup = QtWidgets.QButtonGroup(self)
        self.btnGroup.addButton(self._homeBtn, id=1)
        self.btnGroup.addButton(self._searchBtn, id=2)
        self.btnGroup.idClicked.connect(self.windowLock)

        pixmap = maskImage("./src/mainbkgx.jpg", "jpg", 200, 300, 400, 3)
        self.label_5.setPixmap(pixmap)
        try:
            self._exitBtn.clicked.connect(self.parent().parent().close)
        except:
            self._exitBtn.clicked.connect(self.close)

    def labelPic(self, label: QtWidgets.QLabel, src: str) -> None:
        label.setPixmap(QtGui.QPixmap(src))
        label.setScaledContents(True)

    def windowLock(self, id: int):
        if self._mainWindow == None:
            return
        if id == self._mainWindow.status:
            return
        elif id == 1:
            self._mainWindow.status = 1
            self._mainWindow.update()
        elif id == 2:
            self._homeBtn.setChecked(True)
    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self._mainWindow.status == 1:
            self._homeBtn.setChecked(True)
        else:
            self._searchBtn.setChecked(True)


class TextLabel(QtWidgets.QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        color1 = QtGui.QColor("grey")
        color2 = QtGui.QColor("grey")
        color3 = QtGui.QColor("grey")
        self.parent().labelPic(self.parent().label_6, "./src/Home.png")
        self.parent().labelPic(self.parent().label_7, "./src/ProfileEditM.png")
        self.parent().labelPic(self.parent().label_8, "./src/Exit.png")
        if self.parent().pushButton_4.underMouse() or self.parent().pushButton_4.isChecked():
            color1 = QtGui.QColor("#2F94FD")
            self.parent().labelPic(self.parent().label_6, "./src/HomeM.png")
        if self.parent().pushButton_5.underMouse() or self.parent().pushButton_5.isChecked():
            color2 = QtGui.QColor("#FC7C34")
            self.parent().labelPic(self.parent().label_7, "./src/ProfileEdit.png")
        if self.parent().pushButton_6.underMouse():
            color3 = QtGui.QColor("red")
            self.parent().labelPic(self.parent().label_8, "./src/ExitM.png")
        genFont(painter, "./src/FontWel.ttf", 18, QtCore.QPointF(90,
                110), "HOME", True, color=color1, type="file")
        genFont(painter, "./src/FontWel.ttf", 18, QtCore.QPointF(
            90, 170), "SEARCH", True, color=color2, type="file")
        genFont(painter, "./src/FontWel.ttf", 18, QtCore.QPointF(
            90, 230), "EXIT", True, color=color3, type="file")
        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = FuncBtn()
    win.show()
    app.exec()
