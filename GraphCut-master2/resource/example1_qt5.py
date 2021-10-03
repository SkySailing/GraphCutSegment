import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

def decorator(f):
    def wrapped(self):
        print('get decorated')
        return f(self)
    return wrapped

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 button")
        self.setGeometry(500, 100, 320, 200)
        button = QPushButton('  \n   PyQt5\n   button\n  ', self)
        button.setIcon(QIcon("E:/_Qt/img/qt-logo.png"))
        button.setIconSize(QSize(34, 34))
        button.setToolTip('This is an example button')
        button.setFlat(True)
        button.move(120,70)
        button.clicked.connect(self.on_click)

    @pyqtSlot()
    @decorator
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())