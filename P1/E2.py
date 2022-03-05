#!/usr/bin/python

"""
Practica 1 ISBC

Ejercicio 2

En este ejercicio, genero una ayuda emergente para
el usuario que aparece cuando colocamos el ratón sobre 
el botón

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones 
nuevas de este ejercicio. El resto que aparezcan sin 
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    """
    Constructor de la clase
    """

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        """
        Esta función nos permite ajustar la fuente y el tamaño de la letra
        """

        self.setToolTip('This is a <b>QWidget</b> widget')

        """
        Aquí ajustamos el mensaje que mostrará de la ventana
        """

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        """
        En estas lineas creamos un botón y ajustamos el mensaje
        con la función anterior y las dimensiones
        """

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()

    """
    Creamos una widget instanciando la clase Ejemplo
    """

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
