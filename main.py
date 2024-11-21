import sys
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtCore import Signal

windowWidth, windowHeight = 900, 500

class WelcomeScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.greetings = ["IGR2020", "MOG2129", "AAO2009"]
        self.currentGreeting = 0

        self.button = QtWidgets.QPushButton("Start Wipy")
        self.text = QtWidgets.QLabel("Hello IGR2020", alignment=QtCore.Qt.AlignCenter)

        self.button.clicked.connect(self.start)

        self.layout = QtWidgets.QVBoxLayout(self)


        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

    @QtCore.Slot()
    def start(self):
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = WelcomeScreen()
    widget.resize(windowWidth, windowHeight)
    widget.show()


    sys.exit(app.exec())

