import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon

if __name__ == '__main__' :
    app = QApplication(sys.arg)

    w = QWidget()
    icon = QIcon('testicon.png')
    w.setWindowIcon(icon)
    w.show()

    sys.exit(app.exec_())