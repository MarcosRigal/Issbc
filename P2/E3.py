#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 3

En este ejercicio, creo una calculadora

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        """
        Aquí acabo de crear un grid de botones
        """

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        """
        Aquí creamos las etiquetas que usaremos después
        """

        positions = [(i, j) for i in range(5) for j in range(4)]

        """
        Aquí creo la lista de posiciones del grid
        """

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        """
        Por último, creamos los botones y los agregamos
        """

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
