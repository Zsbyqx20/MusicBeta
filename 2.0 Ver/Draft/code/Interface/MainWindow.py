import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):

    status: int = 1
    keyword: str = ""
    type: int = 0
    onSearch: bool = False
    onShow: bool = False
    SearchStatusChanged = QtCore.pyqtSignal(bool)
    ShowResult = QtCore.pyqtSignal(bool)
    pages:int = 1
    page:int = 1

    def __init__(self):
        super().__init__()
        uic.loadUi("./Interface/MainWindow.ui", self)
        self.setWindowIcon(QtGui.QIcon("./src/MusicBeta.ico"))
        self.anim = None
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.SearchStatusChanged.connect(self.changeSearchStatus)
        self.ShowResult.connect(self.changeShowStatus)
    
    def changeShowStatus(self, status:bool):
        self.onShow = status

    def changeSearchStatus(self, status: bool):
        self.onSearch = status
        
    def labelPic(self, label: QtWidgets.QLabel, src: str) -> None:
        label.setPixmap(QtGui.QPixmap(src))
        label.setScaledContents(True)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.anim == None:
            self.anim = QtCore.QPropertyAnimation(self, b"windowOpacity")
            self.anim.setDuration(800)
            self.anim.setStartValue(1)
            self.anim.setEndValue(0)
            self.anim.finished.connect(self.close)
            self.anim.start()
            a0.ignore()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.oldPosition = a0.globalPosition()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        delta = QtCore.QPointF(a0.globalPosition() - self.oldPosition)
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPosition = a0.globalPosition()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
