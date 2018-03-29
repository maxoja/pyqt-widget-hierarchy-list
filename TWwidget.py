from TWmodel import HierarchicalModel
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QSizePolicy, QLayout, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
import sys
import style


class ItemIcon(QLabel):
    fixedSize = 18

    def __init__(self, path="img/folder.png", parent=None):
        QLabel.__init__(self, parent)
        pix = QPixmap(path)
        pix = pix.scaledToHeight(self.fixedSize)
        self.setPixmap(pix)


class ItemLabel(QLabel):
    family = ".SF NS Text"
    fontSize = 16

    def __init__(self, text, parent=None):
        QLabel.__init__(self, text, parent)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFont(QFont(self.family, self.fontSize))
        self.setStyleSheet(style.normalItemLabel)


class Item(QPushButton):
    leftMargin = 10
    iconTextSpace = 7
    levelIndentSpace = 20

    def __init__(self, text, parent=None, level=0):
        QPushButton.__init__(self,"", parent)

        self.setFixedWidth(250)
        self.setStyleSheet(style.normalItem)

        self.icon = ItemIcon()
        self.label = ItemLabel(text)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.setSpacing(self.iconTextSpace)
        layout.setContentsMargins(self.leftMargin+(level*self.levelIndentSpace), 0, 0, 0)

        layout.addWidget(self.icon)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def setSelected(self, selected):
        if selected:
            self.setStyleSheet(style.selectedItem)
            self.label.setStyleSheet(style.selectedItemLabel)
        else:
            self.setStyleSheet(style.normalItem)
            self.label.setStyleSheet(style.normalItemLabel)

class ItemArea(QScrollArea):
    fixedWidth = 250
    minHeight = 550

    def __init__(self, model, parent=None):
        QScrollArea.__init__(self, parent)
        self.model = model

        self.setFixedWidth(self.fixedWidth)
        self.setMinimumHeight(self.minHeight)
        self.updateGeometry()

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        for i in range(50):
            item = Item("folder-" + str(i*100000), level=(i%3))
            item.clicked.connect(self.onClickItem)
            layout.addWidget(item)

        self.contentSpace = QWidget()
        self.contentSpace.setLayout(layout)

        self.setWidget(self.contentSpace)

    def onClickItem(self):
        for child in self.contentSpace.children():
            if isinstance(child, Item):
                child.setSelected(child == self.sender())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # window = QWidget()
    # scrollarea = QScrollArea()
    # scrollarea.setWidget(ItemArea(None))
    # window.show()
    # scrollarea.show()

    i = ItemArea(None)
    i.show()

    app.setStyleSheet(style.sheet)
    sys.exit(app.exec_())
