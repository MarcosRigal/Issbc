#!/usr/bin/python

"""
Practica 2 ISBC

Actividad: Desarrollo de una aplicación básica

Esta aplicación está diseñada en base a los
requisitos establecidos en la entrega:

 - Menú de opciones
 - Barra de herramientas
 - Barra de estado
 - Una ventana con varios controles dentro

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones 
nuevas de este ejercicio. El resto que aparezcan sin 
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QToolTip,
                             QPushButton, QApplication, QDesktopWidget, QMessageBox, qApp, QMenu, QAction, QLabel)
from PyQt5.QtGui import QFont, QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.i = 0
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('+', self)
        btn.clicked.connect(self.counter_up)
        btn.setToolTip('Increase the counter')
        btn.resize(btn.sizeHint())
        btn.move(50, 125)

        btn2 = QPushButton('-', self)
        btn2.clicked.connect(self.counter_down)
        btn2.setToolTip('Decrease the counter')
        btn2.resize(btn2.sizeHint())
        btn2.move(150, 125)

        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        fileMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        fileMenu.addAction(viewStatAct)

        self.label = QLabel(self)
        self.label.setText("Contador = 0")
        self.label.move(100, 75)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Aplicación Básica')
        self.center()
        self.show()

    def counter_up(self):
        self.i = self.i+1
        self.label.setText("Contador = " + str(self.i))

    def counter_down(self):
        self.i = self.i-1
        self.label.setText("Contador = " + str(self.i))

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:

            event.accept()
        else:

            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
