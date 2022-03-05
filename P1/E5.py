#!/usr/bin/python

"""
Practica 1 ISBC

Ejercicio 5

En este ejercicio, creo una ventana
justo en el centro de la pantalla
sin imporatar el tamaño o resolución

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones 
nuevas de este ejercicio. El resto que aparezcan sin 
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    """
    Esta función, es la encargada de hacer que la ventana
    de nuestro programa aparezca centrada es invocada cuando
    esta se crea en la función initUI ejecutada en el constructor
    """


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
