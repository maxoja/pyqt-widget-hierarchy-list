import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

app = QApplication(sys.argv)

window = QWidget()

grid = QGridLayout()
grid.addWidget(QPushButton("0,0"), 0, 0)
grid.addWidget(QPushButton("0,1"), 0, 1)
grid.addWidget(QPushButton("1,0"), 1, 0)
grid.addWidget(QPushButton("2,2"), 2, 2)

window.setLayout(grid)
window.show()

sys.exit(app.exec_())
