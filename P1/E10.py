#!/usr/bin/python

"""
Practica 1 ISBC

Ejercicio 10

En este ejercicio, creo una pestaña 
con una barra de herramientas que 
incluye un botón que permite cerrar
la aplicación.

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

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        """
        Aquí modelamos el comportamiento del botón
        """

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        """
        Y aquí es donde creamos la barra de herramientas
        a la que le añadimos el botón.
        """

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
