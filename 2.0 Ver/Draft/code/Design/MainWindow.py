import sys
import requests

from typing import List
from PyQt6.QtCore import (QPointF, QPropertyAnimation, Qt,
                          pyqtSignal)
from PyQt6.QtGui import QCloseEvent, QMouseEvent, QPainter, QPaintEvent, QIcon
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QButtonGroup, QWidget)
from PyQt6.uic import loadUi

from Design.tools import buttonImage
from Core.Item import Item


try:
    from Design.tools import *
except:
    from tools import *

ENG_FONT = "Century Gothic"
CHI_FONT = "等线"


class FontLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setInfo(self, item: Item, cur: int, pages: int) -> None:
        self.item = item
        self.curPage = cur
        self.pages = pages
        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        parent: MainWindow = self.parent()
        painter = QPainter(self)
        genFont(painter, ENG_FONT, 12, QPointF(
            350, 310), "by Zsbyqx2020", True)
        if parent.status != 2:
            genFont(painter, ENG_FONT, 24, QPointF(50, 100),
                    "MusicBeta -- 2.0 Version", True)
            if parent.status == 1:
                genFont(painter, ENG_FONT, 18, QPointF(100, 250),
                        "Heading For Your Music...", True)
        else:
            genFont(painter, ENG_FONT, 24, QPointF(
                20, 50), "Searching Result:", True)
            self.item.singer = processName(self.item.singer, 15)
            self.item.album = processName(self.item.album, 7)
            self.item.song = processName(self.item.song, 10)
            genFont(painter, CHI_FONT, 14, QPointF(
                220, 110), f"Song: {self.item.song}")
            genFont(painter, CHI_FONT, 14, QPointF(
                220, 170), f"by:{self.item.singer}")
            genFont(painter, CHI_FONT, 14, QPointF(220, 230),
                    f"collected in:{self.item.album}")
            genFont(painter, CHI_FONT, 12, QPointF(250, 310),
                    f"{self.curPage}/{self.pages}")
        painter.end()


class MainWindow(QMainWindow):

    anim: QPropertyAnimation
    bkgLabel: QLabel
    input: QLineEdit
    fontLabel: FontLabel
    infoLabel: QLabel
    cloudBtn: QPushButton
    kugouBtn: QPushButton
    kuwoBtn: QPushButton
    leftBtn: QPushButton
    rightBtn: QPushButton
    exitBtn: QPushButton
    backBtn: QPushButton
    downloadBtn: QPushButton
    keyword: str
    status: int = 0
    pages: int = 1
    curPage: int = 1
    results: List[Item]
    StatusChanged = pyqtSignal(int)
    PageChanged = pyqtSignal(int)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.basicSetting()
        self.setBackground()
        self.setLabelFont()
        self.setLineEdit()
        self.setFuncBtn()
        self.setInfoLabel()
        self.setSearchMode()
        self.centerWindow()
        self.show()

    def basicSetting(self) -> None:
        self.setGeometry(0, 0, 480, 320)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet('''
            QMainWindow{
                background-color:white;
                border-radius:20px;
            }
            QToolTip{
                background-color:black;
                color:white;
                border:solid 1px black;
            }
        ''')
        self.anim = None
        self.StatusChanged.connect(self.setStatusMode)
        self.PageChanged.connect(self.setCurrentPage)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setStatusMode(self, status: int) -> None:
        self.status = status
        self.update()

    def setCurrentPage(self, delta: int) -> None:
        self.curPage += delta
        self.showResult()

    def setBackground(self) -> None:
        self.bkgLabel = QLabel(self)
        self.bkgLabel.setGeometry(self.geometry())
        pixmap = maskImage("./src/mainbkgx.jpg", "jpg", 480, 320, 155)
        self.bkgLabel.setPixmap(pixmap)
        self.bkgLabel.setScaledContents(True)
        self.bkgLabel.setStyleSheet('''
            border-radius:20px;
        ''')

    def setLineEdit(self) -> None:
        self.input = QLineEdit(self)
        self.input.setGeometry(centerRect(
            self.geometry(), 200, 50, yoffset=0.8))
        self.input.setStyleSheet('''
            QLineEdit {
                border: 1px solid #A0A0A0;
                border-radius: 3px; 
                padding-left: 5px;
                background-color: #F2F2F2; 
                color: #A0A0A0; 
                selection-background-color: #A0A0A0; 
                selection-color: #F2F2F2; 
                font-family: "Microsoft YaHei"; 
                font-size: 14pt; 
            }
        ''')
        self.input.setClearButtonEnabled(True)
        self.input.returnPressed.connect(self.getKeyword)

    def getKeyword(self) -> None:
        self.keyword = self.input.text()

    def setLabelFont(self) -> None:
        self.fontLabel = FontLabel(self)
        self.fontLabel.setGeometry(self.geometry())
        self.fontLabel.setStyleSheet('''
            background-color:transparent;
        ''')

    def setInfoLabel(self) -> None:
        self.infoLabel = QLabel(self)
        self.infoLabel.setGeometry(50, 90, 150, 150)
        self.infoLabel.setStyleSheet('''
            border:2px solid black;
        ''')

    def setFuncBtn(self) -> None:
        self.exitBtn = QPushButton(self)
        self.backBtn = QPushButton(self)
        self.leftBtn = QPushButton(self)
        self.rightBtn = QPushButton(self)
        self.downloadBtn = QPushButton(self)
        btns = [self.backBtn, self.exitBtn, self.leftBtn,
                self.rightBtn, self.downloadBtn]
        srcs = ["back", "exit", "left", "right", "download"]
        for i, btn in enumerate(btns):
            btn.setGeometry(35 * i + 15, 295, 20, 20)
            buttonImage(btn, f"./src/{srcs[i]}.png", "png")
        self.backBtn.clicked.connect(self.backEvent)
        self.exitBtn.clicked.connect(self.close)
        self.leftBtn.clicked.connect(self.turnPage)
        self.rightBtn.clicked.connect(self.turnPage)
        self.downloadBtn.clicked.connect(self.downloadMusic)

    def downloadMusic(self) -> None:
        result = self.results[self.curPage - 1]
        data = requests.get(result.downloadURL).content
        print(f"Music {result.song} start to download...")
        with open(f"{result.album}-{result.song}-{result.singer}.mp3", "wb") as f:
            f.write(data)
        print(f"Music {result.song} downloaded...")

    def turnPage(self) -> None:
        btns = [self.leftBtn, self.rightBtn]
        sender = self.sender()
        delta = 2 * (btns.index(sender)) - 1
        print(f"Current Page:{self.curPage}")
        if self.curPage + delta < 1 or self.curPage + delta > self.pages:
            return
        else:
            self.PageChanged.emit(delta)

    def showResult(self) -> None:
        result = self.results[self.curPage - 1]
        pm = loadWebImage(result.imgData)
        self.fontLabel.setInfo(result, self.curPage, self.pages)
        self.infoLabel.setPixmap(pm)
        self.infoLabel.setScaledContents(True)

    def backEvent(self) -> None:
        if self.status != 2:
            return
        else:
            self.StatusChanged.emit(0)

    def setSearchMode(self) -> None:
        self.modeGroup = QButtonGroup(self)
        self.cloudBtn = QPushButton(self)
        self.kugouBtn = QPushButton(self)
        self.kuwoBtn = QPushButton(self)
        btns = [self.cloudBtn, self.kugouBtn, self.kuwoBtn]
        imgs = ["Cloud", "Kugou", "Kuwo"]
        for i, btn in enumerate(btns):
            btn.setCheckable(True)
            if i == 0:
                btn.setChecked(True)
            self.modeGroup.addButton(btn, id=i)
            btn.setGeometry(55 * i + 170, 150, 30, 30)
            addon = ''
            if btn.isChecked() == False:
                addon = 'W'
            buttonImage(btn, f"./src/{imgs[i]}{addon}.png", "png")
        self.modeGroup.idClicked.connect(self.processMode)

    def processMode(self, id: int) -> None:
        btn = [self.cloudBtn, self.kugouBtn, self.kuwoBtn][id]
        src = ["Cloud", "Kugou", "Kuwo"][id]
        pm = maskImage(f"./src/{src}.png", "png", 30, 30)
        btn.setIcon(QIcon(pm))
        for i, tmpbtn in enumerate([self.cloudBtn, self.kugouBtn, self.kuwoBtn]):
            if i != id:
                pm = maskImage(
                    f"./src/{['Cloud', 'Kugou', 'Kuwo'][i]}W.png", "png", 30, 30)
                tmpbtn.setIcon(QIcon(pm))

    def getResultPage(self, results: List[Item]) -> None:
        self.results = results
        self.pages = len(results)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.oldPosition = a0.globalPosition()

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        delta = QPointF(a0.globalPosition() - self.oldPosition)
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPosition = a0.globalPosition()

    def closeEvent(self, a0: QCloseEvent) -> None:
        if self.anim == None:
            self.anim = QPropertyAnimation(self, b"windowOpacity")
            self.anim.setDuration(800)
            self.anim.setStartValue(1)
            self.anim.setEndValue(0)
            self.anim.finished.connect(self.close)
            self.anim.start()
            a0.ignore()

    def paintEvent(self, a0: QPaintEvent) -> None:
        if self.status == 0:
            self.input.show()
            for btn in self.modeGroup.buttons():
                btn.show()
            self.leftBtn.hide()
            self.rightBtn.hide()
            self.downloadBtn.hide()
            self.infoLabel.hide()
        elif self.status == 1:
            self.input.hide()
            for btn in self.modeGroup.buttons():
                btn.show()
            self.leftBtn.hide()
            self.rightBtn.hide()
            self.downloadBtn.hide()
            self.infoLabel.hide()
        else:
            self.input.hide()
            for btn in self.modeGroup.buttons():
                btn.hide()
            self.leftBtn.show()
            self.rightBtn.show()
            self.downloadBtn.show()
            self.infoLabel.show()
            self.showResult()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    app.exec()
