#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 13

En este ejercicio, creamos un editor de texto básico

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
from pathlib import Path


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        """
        Estas variables van a almacenar la ruta del fichero y su nombre
        """

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
        """
        Aquí comprobamos que la ruta del fichero sea correcta y se haya abierto
        """


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
