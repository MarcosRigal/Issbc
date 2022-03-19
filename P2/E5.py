#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 5

En este ejercicio, asociamos un deslizador
a un contador

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        """
        Con esto conectamos el deslizador con el display
        """

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
