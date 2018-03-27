from PyQt5.QtWidgets import QWidget, QApplication, QToolTip
from PyQt5.QtGui import QFont
import sys

# QToolTip.setFont(QFont('SansSerif', 10))

app = QApplication(sys.argv)

w = QWidget()
w.setToolTip('hello i am <b>tooltip</b>\nfuck you')
w.show()

sys.exit(app.exec_())