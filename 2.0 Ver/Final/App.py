import sys

from PyQt6.QtWidgets import QApplication

from Core.Pipeline import Pipeline
from Core.Spider import Spider
from Design.MainWindow import MainWindow
from Design.tools import *
from threading import Thread


class App(object):

    _win: MainWindow
    _spider: Spider
    _pipe: Pipeline
    _mode: int = 0

    def __init__(self) -> None:
        self._app = QApplication(sys.argv)
        self._win = MainWindow()
        self.connection()

    def connection(self):
        self._win.input.returnPressed.connect(self.getSearchInfo)
        self._win.modeGroup.idClicked.connect(self.getSearchMode)

    def getSearchInfo(self):
        keyword = self._win.input.text()
        names = ['Cloud', 'Kugou', 'Kuwo']
        if keyword == '':
            return

        def emitSignal():
            self._win.StatusChanged.emit(1)

        def search():
            self._spider = Spider(names[self._mode], keyword)
            self._pipe = Pipeline(self._spider)
            self._win.getResultPage(self._pipe.items)
            self._win.StatusChanged.emit(2)
        t1 = Thread(target=search)
        t2 = Thread(target=emitSignal)
        t1.start()
        t2.start()
        t2.join()

    def getSearchMode(self, id: int):
        self._mode = id

    def launch(self):
        self._win.show()
        self._app.exec()


if __name__ == '__main__':
    app = App()
    app.launch()
