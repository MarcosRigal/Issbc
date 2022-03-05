#!/usr/bin/python

"""
Practica 1 ISBC

Ejercicio 7

En este ejercicio, creo una menú
con una opción que permite al usuario
cerrar la pestaña actual

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones 
nuevas de este ejercicio. El resto que aparezcan sin 
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        """
        Estas cuatro lineas son las encargadas de proporcionar
        el comportamiento a la acción de nuestro menú
        """

        self.statusBar()

        """
        Aquí, creo la barra de estado
        """

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        """
        Y aquí es donde configuro el menú,
        añadiendo las distintas acciones
        en concreto exitAct que es la que 
        habíamos creado previamente
        """

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
