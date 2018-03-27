import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout

app = QApplication(sys.argv)

w = QWidget()


okButton = QPushButton('cancel')
cancelButton = QPushButton('cancel')

#by default, adding something to a hbox will push the element from right to left
hBox = QHBoxLayout()
hBox.addStretch(1)          #add an empty space
hBox.addWidget(okButton)
hBox.addWidget(cancelButton)

#by default, push from bottom to top
vBox = QVBoxLayout()
vBox.addStretch(1)
vBox.addLayout(hBox)

w.setLayout(vBox)
w.show()

sys.exit(app.exec_())