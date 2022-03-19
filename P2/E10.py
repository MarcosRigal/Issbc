#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 10

En este ejercicio, conectamos una ventana
emergente con un cuadro de diálogo

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        """
        Aquí creamos la ventana emergente
        """
        if ok:
            self.le.setText(str(text))
        """
        Aquí verificamos si se ha introducido texto
        """

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
