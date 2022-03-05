#!/usr/bin/python

"""
Practica 1 ISBC

Ejercicio 4

En este ejercicio, creo una pestaña de diálogo
que solicita confirmación al usuario para cerrar 
la ventana capturando el evento quit.

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones 
nuevas de este ejercicio. El resto que aparezcan sin 
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:

            event.accept()
        else:

            event.ignore()

    """
    Esta función es la encargada de generar la caja de dialogo,
    para ello, captura el evento y solicita confirmación del
    usuario. En base a lo que este responda, podemos aceptar
    el evento o ignorarlo.
    """


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
