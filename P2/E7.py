#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 7

En este ejercicio, monitorizo la posición
del puntero en tiempo real

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        """
        Aquí definimos las variables que van a 
        almacenar las coordenadas
        """

        self.text = f'x: {x},  y: {y}'

        """
        Aquí defino la etiqueta encargada de mostrar
        el valor de las variables
        """

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        """
        Aquí activamos la monitorización del ratón
        """

        self.setLayout(grid)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = f'x: {x},  y: {y}'
        self.label.setText(text)
        
        """
        Esta función se encarga de actualizar el valor
        de la posición en tiempo real
        """

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
