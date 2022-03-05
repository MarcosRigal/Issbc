#!/usr/bin/python

"""
Practica 1 ISBC

En este ejemplo, creo una 
ventana en PyQt5.

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
"""
Aqui importo los modulos necesarios:
    - sys se utiliza para interactuar con el sistema
    - QApplication y QWidget continene los widgets basicos
"""


def main():

    app = QApplication(sys.argv)
    """
    Aqui creo el objeto de aplicacion de Qt5 necesario para que funcione
    Y le paso, los argumentos que se han mandado a la hora de invocar 
    el script por medio de parametro sys.argv
    """

    window = QWidget()
    window.resize(250, 150)
    window.move(300, 300)
    window.setWindowTitle('E1')
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
