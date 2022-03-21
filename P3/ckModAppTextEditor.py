"""
   Practica 3 ISBC

   Applicación Editor de Texto

   En este fichero se almacena el modelo de la aplicación

   Author: Marcos Rivera Gavilan
   Website: https://www.uco.es/~i92rigam/

   Importante: Para reducir el número de comentarios,
   y simplificar la lectura, solo comentaré las funciones
   nuevas de este ejercicio. El resto que aparezcan sin
   comentar, habrán sido comentadas en ejercicios anteriores.
   """

from pathlib import Path
from PyQt5.QtWidgets import (QFileDialog)
import sys


def selectFolder(self):
    home_dir = str(Path.home())
    self.fileName = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

    if self.fileName[0]:
        file = open(self.fileName[0], 'r')
        return file
