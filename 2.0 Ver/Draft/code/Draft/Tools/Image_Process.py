from PyQt6 import QtCore, QtGui, QtWidgets


def maskImage(imgsrc: str, imgtype: str, w: float, h: float, radius: float, type: int = 1234) -> QtGui.QPixmap:
    imgdata = open(imgsrc, "rb").read()
    image = QtGui.QImage.fromData(imgdata, imgtype)
    image.convertToFormat(QtGui.QImage.Format.Format_ARGB32)
    k = w / h
    if k * image.height() <= image.width():
        actual_h = image.height()
        actual_w = actual_h * k
        rect = QtCore.QRect(
            int((image.width() - actual_w) / 2), 0,
            int(actual_w), int(actual_h)
        )
    else:
        actual_w = image.width()
        actual_h = actual_w / k
        rect = QtCore.QRect(
            0, int((image.height() - actual_h) / 2),
            int(actual_w), int(actual_h)
        )
    image = image.copy(rect)

    out_img = QtGui.QImage(
        actual_w, actual_h, QtGui.QImage.Format.Format_ARGB32)
    out_img.fill(QtCore.Qt.GlobalColor.transparent)

    brush = QtGui.QBrush(image)
    painter = QtGui.QPainter(out_img)
    painter.setBrush(brush)
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)

    if type == 1234:
        painter.drawRoundedRect(QtCore.QRectF(
            0, 0, actual_w, actual_h), radius, radius)
    elif type == 1:
        path = QtGui.QPainterPath()
        path.moveTo(radius, 0)
        path.arcTo(0, 0, 2 * radius, 2 * radius, 180, -90)
        path.lineTo(actual_w, 0)
        path.lineTo(actual_w, actual_h)
        path.lineTo(0, actual_h)
        path.lineTo(0, radius)
        painter.drawPath(path)
    elif type == 4:
        path = QtGui.QPainterPath()
        path.moveTo(0, 0)
        path.lineTo(actual_w, 0)
        path.lineTo(actual_w, actual_h - radius)
        path.arcTo(actual_w - 2 * radius, actual_h - 2 * radius, 2 * radius, 2 * radius, 0, -90)
        path.lineTo(0, actual_h)
        path.lineTo(0, 0)
        painter.drawPath(path)
    elif type == 3:
        path = QtGui.QPainterPath()
        path.moveTo(0, 0)
        path.lineTo(0, actual_h - radius)
        path.arcTo(0, actual_h - 2 * radius, 2 * radius, 2 * radius, 180, 90)
        path.lineTo(actual_w, actual_h)
        path.lineTo(actual_w, 0)
        path.lineTo(0, 0)
        painter.drawPath(path)
    painter.end()

    pr = QtGui.QWindow().devicePixelRatio()
    pm = QtGui.QPixmap.fromImage(out_img)
    pm.setDevicePixelRatio(pr)
    w *= pr
    h *= pr
    pm = pm.scaled(int(w), int(h), QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                   QtCore.Qt.TransformationMode.SmoothTransformation)

    return pm
