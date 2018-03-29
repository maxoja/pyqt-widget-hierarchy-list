from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPen, QPainter, QPolygonF, QColor, QBrush
from PyQt5.QtCore import QTimer, QPointF, Qt, QLineF
from math import *

import sys

class Vertice:
    def __init__(self, x1, y1, x2, y2):
        self.sx = x1
        self.dx = x2-x1
        self.sy = y1
        self.dy = y2-y1

    def lerp(self, r, scale=1):
        return scale*(self.sx + self.dx*r), scale*(self.sy + self.dy*r)

class DropDownArrow(QWidget):
    step = 0.01

    def __init__(self, parent=None, size=12, speed=25, color=QColor(0,0,0), selected=False, updateEquation='self.dir * abs(self.x+0.01)**0.75*self.step*self.speed', kernel="self.x", onDown=None, onUp=None):
        QWidget.__init__(self, parent)

        self.setFixedSize(size, size)
        self.speed = speed
        self.color = color
        self.updateEquation = updateEquation
        self.kernel = kernel
        self.selected = selected
        self.changing = False
        self.hiding = False
        self.x = 1 if selected else 0
        self.onDown = onDown
        self.onUp = onUp

        self.verts = [
            Vertice(0.2, 0.1,   0.9, 0.3),
            Vertice(0.2, 0.9,   0.1,   0.3),
            Vertice(0.9, 0.5, 0.5,   0.8)
        ]

        timer = QTimer(self)
        timer.timeout.connect(self.onTick)
        timer.start(20)

    def setSelected(self, selected):
        if selected != self.selected:
            self.changing = True

        self.selected = selected

    def setHideVisual(self, hiding):
        self.hiding = hiding

    def isSelected(self):
        return self.selected

    def toggle(self):
        self.setSelected(not self.isSelected())

    def setColor(self, color):
        assert(isinstance(color, QColor))
        self.color = color

    def paintEvent(self, event):
        color = self.color if not self.hiding else QColor(0,0,0,0)

        pen = QPen()
        pen.setWidth(self.width()/8)
        pen.setCapStyle(Qt.RoundCap)
        pen.setColor(color)

        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(color)

        painter = QPainter(self)
        painter.setPen(pen)
        painter.setBrush(brush)

        points = [ QPointF(*v.lerp(eval(self.kernel), self.width())) for v in self.verts ]
        painter.drawLine(QLineF(points[0],points[1]))
        painter.drawLine(QLineF(points[1],points[2]))
        painter.drawLine(QLineF(points[2],points[0]))

        poly = QPolygonF(points)
        painter.drawPolygon(poly)

    def onTick(self):

        if self.selected:
            self.begin = 0
            self.end = 1
            self.dir = 1
        else:
            self.begin = 1
            self.end = 0
            self.dir = -1

        self.x += eval(self.updateEquation)

        if self.x <= 0 and not self.selected:
            self.x = 0

            if self.onUp:
                if self.changing:
                    self.changing = False
                    self.onUp()
            else:
                self.changing=False

        if self.x >= 1 and self.selected:
            self.x = 1

            if self.onDown:
                if self.changing:
                    self.changing = False
                    self.onDown()
            else:
                self.changing = False

        self.update()