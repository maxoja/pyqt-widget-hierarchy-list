from TModel import HierarchicalModel
from TWidget import HierarchyPanel
from PyQt5.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    tree = HierarchicalModel()
    tree.add(0, name="root", tip="testtip\nhello world!")
    tree.add(1, 0, name="3D models", tip="testtip\nhello world!")
    tree.add(2, 1, name="Weapons", tip="testtip\nhello world!")
    tree.add(3, 2, name="Guns", tip="testtip\nhello world!")
    tree.add(4, 2, name="Melees", tip="testtip\nhello world!")
    tree.add(5, 2, name="Bombs", tip="testtip\nhello world!")
    tree.add(24, 1, name="Furnitures", tip="testtip\nhello world!")
    tree.add(25, 1, name="Instruments", tip="testtip\nhello world!")
    tree.add(26, 1, name="Zombies", tip="testtip\nhello world!")
    tree.add(6, 1, name="Vehicles", tip="testtip\nhello world!")
    tree.add(7, 6, name="Boats", tip="testtip\nhello world!")
    tree.add(8, 6, name="Bikes", tip="testtip\nhello world!")
    tree.add(9, 1, name="Trees", tip="testtip\nhello world!")
    tree.add(10, 0, name="Sprite Sheets", tip="testtip\nhello world!")
    tree.add(11, 10, name="Characters", tip="testtip\nhello world!")
    tree.add(12, 10, name="Buildings", tip="testtip\nhello world!")
    tree.add(13, 10, name="Map-Tiles", tip="testtip\nhello world!")
    tree.add(14, 10, name="Buttons", tip="testtip\nhello world!")
    tree.add(15, 10, name="Obstacles", tip="testtip\nhello world!")
    tree.add(16, 10, name="Magics", tip="testtip\nhello world!")
    tree.add(17, 10, name="Bullets&Rockets", tip="testtip\nhello world!")
    tree.add(18, 10, name="Lights", tip="testtip\nhello world!")
    tree.add(19, 10, name="Effects", tip="testtip\nhello world!")
    tree.add(20, 10, name="Titles", tip="testtip\nhello world!")
    tree.add(21, 10, name="9-Patches", tip="testtip\nhello world!")
    tree.add(22, 10, name="HUD", tip="testtip\nhello world!")
    tree.add(23, 10, name="Bars", tip="testtip\nhello world!")

    panel = HierarchyPanel(tree)
    panel.show()

    sys.exit(app.exec_())