from TWmodel import HierarchicalModel
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QSizePolicy, QLayout, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QColor
from dropdown import DropDownArrow

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
    leftMargin = 7
    iconTextSpace = 5
    levelIndentSpace = 20
    fixedWidth = 250

    def __init__(self, id, text, parent=None, level=0, expandable=False):
        QPushButton.__init__(self,"", parent)
        self.id = id
        self.highlighted = False
        self.selected = False
        self.level = level

        self.setFixedWidth(self.fixedWidth)
        self.setStyleSheet(style.normalItem)

        self.icon = ItemIcon()
        self.label = ItemLabel(text)
        self.arrow = DropDownArrow()
        if not expandable: self.arrow.setHideVisual(True)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.setSpacing(self.iconTextSpace)
        layout.setContentsMargins(self.leftMargin+(level*self.levelIndentSpace), 0, 0, 0)

        layout.addWidget(self.arrow)
        layout.addWidget(self.icon)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def setHighlighted(self, highlighted):
        self.highlighted = highlighted

        if highlighted:
            self.arrow.setColor(QColor(220,220,220))
            self.setStyleSheet(style.selectedItem)
            self.label.setStyleSheet(style.selectedItemLabel)
        else:
            self.arrow.setColor(QColor(0,0,0))
            self.setStyleSheet(style.normalItem)
            self.label.setStyleSheet(style.normalItemLabel)

    def setSelected(self, selected):
        self.selected = selected
        self.arrow.setSelected(selected)
        color = QColor(220,220,220) if selected else QColor(0,0,0)
        self.arrow.setColor(color)

    def isHighlighted(self):
        return self.highlighted

    def isSelected(self):
        return self.selected

    def getId(self):
        return self.id

class ItemArea(QScrollArea):
    fixedWidth = 250
    minHeight = 550

    def __init__(self, model, parent=None):
        QScrollArea.__init__(self, parent)
        self.model = model
        self.expanding = { i:False for i in self.model.getIds() }
        self.itemDict = dict()

        self.setFixedWidth(self.fixedWidth)
        self.setMinimumHeight(self.minHeight)
        self.updateGeometry()

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout.setSizeConstraint(QLayout.SetMinAndMaxSize)

        rootId = 0
        self.construct(layout, rootId, 0)

        self.contentSpace = QWidget()
        self.contentSpace.setLayout(layout) ##layout added here

        self.setWidget(self.contentSpace)

    def construct(self, layout, id, level):
        for childId in self.model.getChildrenOf(id, getIdOnly=True):
            dirItem = self.model.getDir(childId)
            dirExpandable = self.model.hasChildren(childId)
            listItem = Item(id, "folder-" + dirItem, level=level, expandable=dirExpandable)
            listItem.clicked.connect(self.onClickItem)
            layout.addWidget(listItem)
            self.itemDict[childId] = listItem

            if level != 0:
                listItem.hide()

            self.construct(layout, childId, level+1)

    def expandItem(self, id, expanding):
        listItem = self.itemDict[id]
        listItem.setSelected(expanding)

        for childId in self.model.getChildrenOf(id, getIdOnly=True):
            childItem = self.itemDict[childId]

            if expanding :
                childItem.show()
            else :
                self.expandItem(childId, expanding)
                childItem.hide()

    def onClickItem(self):
        for childId, child in self.itemDict.items() :
            if child != self.sender():
                child.setHighlighted(False)
            else:
                if child.isHighlighted():
                    if child.isSelected():
                        child.setSelected(False)
                        self.expandItem(childId, False)
                    else:
                        child.setSelected(True)
                        child.arrow.onDown = lambda i=childId: self.expandItem(i, True)

                child.setHighlighted(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree = HierarchicalModel()
    tree.add(0, item="root")
    tree.add(1, 0, item="3D models")
    tree.add(2, 1, item="Weapons")
    tree.add(3, 2, item="Guns")
    tree.add(4, 2, item="Melees")
    tree.add(5, 2, item="Bombs")
    tree.add(24, 1, item="Furnitures")
    tree.add(25, 1, item="Instruments")
    tree.add(26, 1, item="Zombies")
    tree.add(6, 1, item="Vehicles")
    tree.add(7, 6, item="Boats")
    tree.add(8, 6, item="Bikes")
    tree.add(9, 1, item="Trees")
    tree.add(10, 0, item="Sprite Sheets")
    tree.add(11, 10, item="Characters")
    tree.add(12, 10, item="Buildings")
    tree.add(13, 10, item="Map-Tiles")
    tree.add(14, 10, item="Buttons")
    tree.add(15, 10, item="Obstacles")
    tree.add(16, 10, item="Magics")
    tree.add(17, 10, item="Bullets&Rockets")
    tree.add(18, 10, item="Lights")
    tree.add(19, 10, item="Effects")
    tree.add(20, 10, item="Titles")
    tree.add(21, 10, item="9-Patches")
    tree.add(22, 10, item="HUD")
    tree.add(23, 10, item="Bars")

    i = ItemArea(tree)
    i.show()


    # window = QWidget()
    # scrollarea = QScrollArea()
    # scrollarea.setWidget(ItemArea(None))
    # window.show()
    # scrollarea.show()

    app.setStyleSheet(style.sheet)
    sys.exit(app.exec_())
