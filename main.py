from TModel import HierarchicalModel
from TWidget import HierarchyPanel
from PyQt5.QtWidgets import QApplication

import sys

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



