#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 9

En este ejercicio, hacemos que se cierre la
pestaña al hacer click

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):

    closeApp = pyqtSignal()


"""
Creamos una clase para la señal de cerrar
Creamos una nueva señal como un atributo de la clase
"""


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        """
        Asociamos la señal a cerrar
        """

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):

        self.c.closeApp.emit()
    """
    Definimos esta función para que cuando se
    haga click se cierre la aplicación
    """


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
