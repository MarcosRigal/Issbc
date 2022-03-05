#!/usr/bin/python

"""
Practica 1 ISBC

Ejercicio 1

En este ejercicio, creo una
ventana en PyQt5.

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
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

    """
    En este punto, hemos creado la ventana y ajustamdo las dimensiones
    """

    sys.exit(app.exec_())

    """
    Esta función hace que entremos en el bucle de ejecución en el que
    permaneceremos hasta que cerremos la ventana.
    """

if __name__ == '__main__':
    main()

"""
Este bloque de código invoca a la función main del programa
que contiene el código principal del programa. El interprete
de Python empieza por aquí
"""
