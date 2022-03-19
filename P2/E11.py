#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 11

En este ejercicio, creamos un cuadro de 
diálogo que nos permite escoger un color

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        """
        Aquí creamos una variable que almacena el color
        """

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 200, 200)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        """
        Esto invoca al cuadro de diálogo para seleccionar el color
        """

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }'
                                   % col.name())

        """
        Esta función valida que el color introducido sea válido
        """


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
