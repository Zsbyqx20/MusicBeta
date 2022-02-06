import sys
import math
from threading import Thread

from PyQt6 import QtCore, QtGui, QtWidgets
from numpy import ceil

from Core.Pipeline import Pipeline
from Core.Spider import Spider
from Interface.MainWindow import MainWindow

sys.path.append("./Interface")


class Engine(object):
    _spider: Spider
    _pipe: Pipeline
    _window: MainWindow

    def __init__(self) -> None:
        self._app = QtWidgets.QApplication(sys.argv)
        self._window = MainWindow()
        self._mainBKG = self._window.widget_4
        self._lineEdit: QtWidgets.QLineEdit = self._mainBKG.lineEdit
        self._btnGroup: QtWidgets.QButtonGroup = self._window.widget_5.btnGroup
        self._name = "Cloud"
        self._btnGroup.idClicked.connect(self.searchType)
        self._lineEdit.returnPressed.connect(self.searchKeyword)
        self._mainBKG.label_1.setEngine(self)

    def launch(self):
        self._window.show()
        self._app.exec()

    def searchKeyword(self) -> None:
        self._window.status = 2
        self._window.ShowResult.emit(False)
        self._keyword = self._lineEdit.text()
        self._window.keyword = self._keyword
        if self._keyword == '':
            return
        t1 = Thread(target=self.onSearching)
        t2 = Thread(target=self.search)
        t1.start()
        t2.start()
        t1.join()

    def onSearching(self):
        self._mainBKG.label_5.setVisible(True)
        self._window.SearchStatusChanged.emit(True)

    def searchType(self, id: int) -> None:
        self._name = ["Cloud", "Kugou", "Kuwo"][id]

    def search(self) -> None:
        print("Start Searching...")
        self._spider = Spider(self._name, self._keyword)
        self._pipe = Pipeline(self._spider)
        print("Search Over!")
        self._window.pages = math.ceil(len(self._pipe.items) / 2)
        self._window.SearchStatusChanged.emit(False)
        self._window.ShowResult.emit(True)
        self._mainBKG.label_5.setVisible(False)


if __name__ == '__main__':
    eng = Engine()
    eng.launch()
