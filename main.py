import sys
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

windowWidth, windowHeight = 900, 500

class Image(QtWidgets.QLabel):
    def __init__(self, path: str, scale: int = 1, **kwargs):
        super().__init__(**kwargs)

        pixelMap = QtGui.QImage(path)
        imageWidth, imageHeight = pixelMap.width(), pixelMap.height()
        pixelMap = pixelMap.scaled(imageWidth*scale, imageHeight*scale)
        self.setPixmap(QtGui.QPixmap.fromImage(pixelMap))

class App(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.addWidget(WelcomeScreen(self))
        self.addWidget(Editor(self))

        self.setCurrentIndex(0)

class WelcomeScreen(QtWidgets.QWidget):
    def __init__(self, parentApp: QtWidgets.QStackedWidget):
        super().__init__()
        self.parentApp = parentApp

        self.button = QtWidgets.QPushButton("Start Wipy")
        self.text = QtWidgets.QLabel("Welcome To Wipy", alignment=QtCore.Qt.AlignCenter)

        self.button.clicked.connect(self.start)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

    @QtCore.Slot()
    def start(self):
        self.parentApp.setCurrentIndex(1)


class Editor(QtWidgets.QWidget):
    def __init__(self, parentApp: QtWidgets.QStackedWidget):
        super().__init__()
        self.parentApp = parentApp

        self.image = Image("Texture.png", 10, alignment=QtCore.Qt.AlignCenter)

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.image)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = App()
    widget.resize(windowWidth, windowHeight)
    widget.show()


    sys.exit(app.exec())

