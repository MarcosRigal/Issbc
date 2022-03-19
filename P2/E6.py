#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 6

En este ejercicio, hacemos que al pulsar
esc se cierre la app

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    """
    Esta función asocia la tecla escape con la acción
    de cerrar la ventana
    """


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
