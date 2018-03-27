#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    '''
    create an application object. 
    The sys.argv parameter is a list of arguments from a command line. 
    Python scripts can be run from the shell. 
    It is a way how we can control the startup of our scripts. 
    '''
    app = QApplication(sys.argv)

    '''
    *!* A widget with no parent is called a window. *!*
    QWidget widget is the base class of all user interface objects in PyQt5. 
    The default constructor has no parent. 
    '''
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')

    '''
    displays the widget on the screen. 
    A widget is first created in memory 
    and later shown on the screen.
    '''
    w.show()

    '''
    exec_() to enter main loop of the app
    the events handling start from this point
    sys.exit() to make clean exit
    '''
    sys.exit(app.exec_())