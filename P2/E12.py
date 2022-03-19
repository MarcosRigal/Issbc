
#!/usr/bin/python

"""
Practica 2 ISBC

Ejercicio 12

En este ejercicio, creamos un cuadro de
diálogo para escoger la fuente

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):

        font, ok = QFontDialog.getFont()

        """
        Aquí hemos declarado las variables que van a 
        almacenar lo que devuelva el cuadro de diálogo.
        """

        if ok:
            self.lbl.setFont(font)
        """
        Aquí comprobamos que la nueva fuente sea válida 
        y si lo es, la cambiamos en el programa
        """


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
