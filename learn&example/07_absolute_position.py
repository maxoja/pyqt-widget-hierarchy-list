import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()

    label1 = QLabel("label 1 text", window)
    label2 = QLabel("label 2 text", window)
    label3 = QLabel("label 3 text", window)

    #use move and setGeometry to arrange stuff
    window.setGeometry(100,10, 200,300)
    label1.move(15,10)
    label2.move(30,20)
    label3.move(35,25)

    window.show()

    sys.exit(app.exec_())