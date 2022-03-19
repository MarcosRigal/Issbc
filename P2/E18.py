#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 18

En este ejercicio, creamos un
calendario para el usuario

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        """
        Creamos el widget calendario
        """
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        """
        Permite que seleccionemos una fecha
        """

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())

    """
    Se encarga de parsear la fecha seleccionada a texto
    """


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
