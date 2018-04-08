from TModel import HierarchicalModel
from TWidget import DropDownArrow
import TWidget.style as style

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QSizePolicy, QLayout, QHBoxLayout, QScrollArea, QToolTip
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QColor

import sys


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

    arrowEq = 'self.dir * abs(self.x+0.01)**0.75*self.step*self.speed'
    arrowKernel = 'sin(self.x*3.14/2)'
    arrowSize = 12
    arrowSpeed = 25

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
        self.arrow = DropDownArrow(size=self.arrowSize, speed=self.arrowSpeed, updateEquation=self.arrowEq, kernel=self.arrowKernel)
        if not expandable:
            self.arrow.setHideVisual(True)

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
            self.setStyleSheet(style.highlightedItem)
            self.label.setStyleSheet(style.highlightedItemLabel)
        else:
            self.arrow.setColor(QColor(0,0,0))
            self.setStyleSheet(style.normalItem)
            self.label.setStyleSheet(style.normalItemLabel)

    def setSelected(self, selected):
        self.selected = selected
        self.arrow.setSelected(selected)
        color = QColor(220,220,220) if self.highlighted else QColor(0,0,0)
        self.arrow.setColor(color)

    def isHighlighted(self):
        return self.highlighted

    def isSelected(self):
        return self.selected

    def getId(self):
        return self.id


class HierarchyPanel(QScrollArea):
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
        self.__construct(layout, rootId, 0)

        self.contentSpace = QWidget()
        self.contentSpace.setLayout(layout) ##layout added here

        self.setWidget(self.contentSpace)

    def __construct(self, layout, id, level):
        if id not in self.expanding:
            self.__expandItem[id] = False

        for childId in self.model.getChildrenOf(id, getIdOnly=True):

            itemModel = self.model.getItemOf(childId)
            itemExpandable = self.model.hasChildren(childId)
            itemName = self.model.getNameOf(childId)

            listItem = Item(childId, itemName, level=level, expandable=itemExpandable)
            if 'tip' in itemModel :
                listItem.setToolTip(itemModel['tip'])
            listItem.clicked.connect(self.__onClickItem)
            layout.addWidget(listItem)
            self.itemDict[childId] = listItem

            if level != 0:
                listItem.hide()

            self.__construct(layout, childId, level + 1)

    def reconstruct(self, rootId):
        for k, i in self.itemDict.items():
            i.setParent(None)
            self.contentSpace.layout().removeWidget(i)

        self.itemDict = dict()
        self.__construct(self.contentSpace.layout(), rootId, 0)

        for i in self.itemDict:
            if self.expanding[i]:
                self.__expandItem(i, True)

    def getHighlightedItem(self):
        for i in self.itemDict.values():
            if i.isHighlighted():
                return i

        return None

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_D:
    #         item = self.getHighlightedItem()
    #         if item is None:
    #             return
    #         self.model.removeById(item.getId())
    #         self.reconstruct(0)


    def __expandItem(self, id, expanding):
        self.expanding[id] = expanding
        listItem = self.itemDict[id]
        listItem.setSelected(expanding)

        for childId in self.model.getChildrenOf(id, getIdOnly=True):
            childItem = self.itemDict[childId]

            if expanding :
                childItem.show()
            else :
                self.__expandItem(childId, expanding)
                childItem.hide()

    def __onClickItem(self):
        for childId, child in self.itemDict.items() :
            if child != self.sender():
                child.setHighlighted(False)
            else:
                if child.isHighlighted():
                    if child.isSelected():
                        child.setSelected(False)
                        self.__expandItem(childId, False)
                    else:
                        child.setSelected(True)
                        child.arrow.onDown = lambda i=childId: self.__expandItem(i, True)

                child.setHighlighted(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree = HierarchicalModel()
    tree.add(0, name="root")\
        .add(1, 0, name="3D models", tip="you can set tooltip text\nby passing tip value of item")\
            .add(2, 1, name="Weapons")\
                .add(3, 2, name="Guns")\
                .add(4, 2, name="Melees")\
                .add(5, 2, name="Bombs")\
            .add(24, 1, name="Furnitures")\
            .add(25, 1, name="Instruments")\
            .add(26, 1, name="Zombies")\
            .add(6, 1, name="Vehicles")\
                .add(7, 6, name="Boats")\
                .add(8, 6, name="Bikes")\
            .add(9, 1, name="Trees")\
        .add(10, 0, name="Sprite Sheets")\
            .add(11, 10, name="Characters")\
            .add(12, 10, name="Buildings")\
            .add(13, 10, name="Map-Tiles")\
            .add(14, 10, name="Buttons")\
            .add(15, 10, name="Obstacles")\
            .add(16, 10, name="Magics")\
            .add(17, 10, name="Bullets&Rockets")\
            .add(18, 10, name="Lights")\
            .add(19, 10, name="Effects")\
            .add(20, 10, name="Titles")\
            .add(21, 10, name="9-Patches")\
            .add(22, 10, name="HUD")\
            .add(23, 10, name="Bars")

    panel = HierarchyPanel(tree)
    panel.show()

    sys.exit(app.exec_())




