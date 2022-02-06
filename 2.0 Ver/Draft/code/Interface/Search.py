import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic

from Tools.genFont import genFont
from Tools.Image_Process import maskImage
from Interface.MainWindow import MainWindow


class Search_Options(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./Interface/Search_Options.ui", self)
        self.textLink = ["Cloud", "Kugou", "Kuwo"]
        self.labelLink = [self.label_3, self.label_4, self.label_5]
        try:
            self._mainWindow:MainWindow = self.parent().parent()
        except:
            self._mainWindow = None
        
        pixmap = maskImage("./src/mainbkgx.jpg", "jpg", 250, 352, 400, type=4)
        self.label_2.setPixmap(pixmap)
        
        self.labelPic(self.label_3, "./src/Cloud.png")
        self.labelPic(self.label_4, "./src/KugouW.png")
        self.labelPic(self.label_5, "./src/KuwoW.png")
        
        self.btnGroup = QtWidgets.QButtonGroup(self)
        self.btnGroup.addButton(self.pushButton_1, id=0)
        self.btnGroup.addButton(self.pushButton_2, id=1)
        self.btnGroup.addButton(self.pushButton_3, id=2)
        self.btnGroup.idClicked.connect(self.changeImage)

    def changeImage(self, id: int):
        self._mainWindow.type = id
        name = self.textLink[id]
        label = self.labelLink[id]
        self.labelPic(label, f"./src/{name}.png")
        for i in range(3):
            if i == id:
                continue
            else:
                self.labelPic(self.labelLink[i],
                              f"./src/{self.textLink[i]}W.png")
        self.update()

    def labelPic(self, label: QtWidgets.QLabel, src: str) -> None:
        label.setPixmap(QtGui.QPixmap(src))
        label.setScaledContents(True)


class PaintLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.textLink = {
            "pushButton_1": "CLOUD",
            "pushButton_2": "KUGOU",
            "pushButton_3": "KUWO"
        }

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        self.colorDesign(painter)
        self.fontDesign(painter)
        self.btnDesign(painter)
        painter.end()

    def fontDesign(self, painter: QtGui.QPainter) -> None:
        genFont(painter, "Century Gothic", 20,
                QtCore.QPointF(15, 200), "Search", True)
        genFont(painter, "Century Gothic", 20, QtCore.QPointF(
            130, 170), "Options", True, QtGui.QColor("white"))

    def colorDesign(self, painter: QtGui.QPainter) -> None:
        path = QtGui.QPainterPath()
        path.moveTo(0, 148)
        path.cubicTo(150, 148, 187.5, 273, 250, 148)
        path.lineTo(250, 25)
        path.arcTo(200, 0, 50, 50, 0, 90)
        path.lineTo(0, 0)
        path.lineTo(0, 148)
        color = QtGui.QLinearGradient(0, 0, 0, 250)
        color.setColorAt(0, QtGui.QColor("#878299"))
        color.setColorAt(1, QtGui.QColor("#A0A1B3"))
        painter.setBrush(color)
        painter.setPen(QtCore.Qt.GlobalColor.transparent)
        painter.drawPath(path)
        painter.setPen(QtGui.QPen(QtGui.QColor("#8B8C9E")))
        path.moveTo(0, 148)
        path.cubicTo(150, 148, 187.5, 273, 250, 148)
        painter.drawPath(path)

    def btnDesign(self, painter: QtGui.QPainter) -> None:
        for tmpbtn in self.parent().btnGroup.buttons():
            rect = tmpbtn.geometry()
            if tmpbtn.isChecked():
                painter.setPen(QtGui.QPen(QtGui.QColor("white"), 4))
                color = QtGui.QColor(139, 140, 158)
            elif tmpbtn.underMouse():
                color = QtGui.QColor(139, 140, 158, 200)
                painter.setPen(QtCore.Qt.GlobalColor.transparent)
            else:
                color = QtGui.QColor(139, 140, 158, 150)
                painter.setPen(QtCore.Qt.GlobalColor.transparent)
            painter.setBrush(color)
            painter.drawRoundedRect(rect, 15, 15)


class TextButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.textLink = {
            "pushButton_1": "CLOUD",
            "pushButton_2": "KUGOU",
            "pushButton_3": "KUWO"
        }
        self.pointLink = {
            "pushButton_1": QtCore.QPointF(21, 45),
            "pushButton_2": QtCore.QPointF(21, 45),
            "pushButton_3": QtCore.QPointF(26, 45),
        }
        self.colorLink = {
            "pushButton_1": "red",
            "pushButton_2": "#2F94FD",
            "pushButton_3": "#FC7C34"
        }

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        text = self.textLink[self.objectName()]
        if self.isChecked():
            color = QtGui.QColor(self.colorLink[self.objectName()])
        else:
            color = QtGui.QColor("gray")
        genFont(painter, "./src/FontWel.ttf", 20,
                self.pointLink[self.objectName()], text, type="file", color=color)
        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Search_Options()
    win.show()
    app.exec()
