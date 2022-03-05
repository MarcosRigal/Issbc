#!/usr/bin/python

"""
Practica 1 ISBC

Ejercicio 9

Este ejercicio, es una variante del ejercicio 7
solo que en vez de tener un botón en el submenú,
hay una checkbox que permite activar y desactivar
la barra de estado.

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones 
nuevas de este ejercicio. El resto que aparezcan sin 
comentar, habrán sido comentadas en ejercicios anteriores.
"""


import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        """
        Similar al código del ejercicio 7 solo
        que en este caso utilizamos un toggleMenu
        """

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


    """
    Esta función, es la encargada de modelar el comportamiento
    del botón mostrando y ocultando la barra de estado en función
    de la opción seleccionada.
    """

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
