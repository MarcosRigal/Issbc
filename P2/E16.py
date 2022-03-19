 #!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 16

En este ejercicio, creamos un deslizador
que permite subir y bajar el volumen

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)

        """
        Aquí creamos el deslizador
        """

        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(250, 40, 80, 30)

        """
        Posicionamos el icono de volumen y lo ponemos en mute por defecto
        """

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:

            self.label.setPixmap(QPixmap('mute.png'))
        elif 0 < value <= 30:

            self.label.setPixmap(QPixmap('min.png'))
        elif 30 < value < 80:

            self.label.setPixmap(QPixmap('med.png'))
        else:

            self.label.setPixmap(QPixmap('max.png'))
    """
    Esta función es la que cambia el icono cuando el
    usuario sube y baja el volumen con el deslizador
    """

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()