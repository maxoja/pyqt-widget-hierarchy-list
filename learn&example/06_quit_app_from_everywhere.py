from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys

def call_quit() :
    QApplication.instance().quit()

app = QApplication(sys.argv)

w = QWidget()
b = QPushButton('Quit', w)
b.clicked.connect(call_quit)
w.show()

sys.exit(app.exec_())