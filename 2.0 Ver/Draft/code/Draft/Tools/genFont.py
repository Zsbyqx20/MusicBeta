from PyQt6 import QtCore, QtGui, QtWidgets
import typing


def genFont(painter: QtGui.QPainter,
            src: str, size: int,
            point: QtCore.QPointF,
            content: str,
            isBold: bool = False,
            color: typing.Union[QtGui.QColor, QtGui.QLinearGradient] = None,
            type: str = "name",
            rotate: float = 0,) -> None:
    if color == None:
        color = QtCore.Qt.GlobalColor.black
    path = QtGui.QPainterPath()
    if type == "file":
        fontID = QtGui.QFontDatabase.addApplicationFont('./src/FontWel.ttf')
        target = QtGui.QFontDatabase.applicationFontFamilies(fontID)[0]
    else:
        target = src
    font = QtGui.QFont(target, size)
    if isBold == True:
        font.setBold(True)
    path.addText(point, font, content)
    painter.rotate(rotate)
    painter.setBrush(QtGui.QBrush(color))
    painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.transparent))
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    painter.drawPath(path)
    painter.rotate(-rotate)
