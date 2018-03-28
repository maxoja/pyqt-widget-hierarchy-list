from TWmodel import HierarchicalModel
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import sys

class HierarchicalItemWidget(QPushButton) :
    styleString = '''
        HierarchicalItemWidget:pressed {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))
        }
        HierarchicalItemWidget {
             background-color: #3cbaa2; border: 0.1px solid black;
             border-radius: 0px;
        }

        HierarchicalItemWidget:disabled {
            # background-color: rgb(170, 170, 127)
        }
    '''

    fixedHeight = 28
    fixedWidth = 200
    iconPath = "test.png"
    xPadding = 6
    yPadding = 3

    def __init__(self, text="", parent=None):
        QPushButton.__init__(self, "", parent)
        self.setFixedHeight(self.fixedHeight)
        self.setMinimumWidth(self.fixedWidth)
        self.setStyleSheet(self.styleString)

        self.pix = QPixmap(self.iconPath)
        self.icon = QLabel(self)
        self.label = QLabel(text, self)

        self.__adjustIcon()
        self.__adjustLabel()

    def resizeEvent(self, a0):
        # self.__adjustIcon()
        self.__adjustLabel()

    def __adjustIcon(self):
        pixGeo = self.__getRefinedIconGeomatrix(self.pix)
        newPix = self.pix.scaledToHeight(pixGeo[3])
        self.icon.setGeometry(*pixGeo)
        self.icon.setPixmap(newPix)


    def __getRefinedIconGeomatrix(self, pix):
        newWidth = self.height() - self.xPadding*2
        newHeight = pix.width() * (newWidth) / pix.height()
        return ( self.xPadding, self.yPadding, newHeight, newWidth )

    def __adjustLabel(self):
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        l = self.xPadding + self.icon.pixmap().width() + self.xPadding
        t = self.yPadding
        w = self.width()-l-self.xPadding
        h = self.height()-2*self.yPadding
        self.label.setGeometry(l,t,w,h)



app = QApplication(sys.argv)

window = QWidget()

layout = QVBoxLayout()
layout.setContentsMargins(0,1,0,1)
layout.setSpacing(1)
for i in range(1,20) :
    layout.addWidget(HierarchicalItemWidget(str(i*100000)))
    layout.addWidget(HierarchicalItemWidget(str(i*100000)))

window.setLayout(layout)
window.show()

sys.exit(app.exec_())