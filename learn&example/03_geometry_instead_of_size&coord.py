import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__' :
    app = QApplication(sys.argv)

    w = QWidget()
    w.setGeometry(0,0,1,500)
    w.show()

    sys.exit(app.exec_());
