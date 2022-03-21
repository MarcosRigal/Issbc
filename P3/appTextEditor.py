"""
Practica 3 ISBC

Applicación Editor de Texto

Con este fichero iniciamos la aplicación

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

import sys
from PyQt5 import QtWidgets
import ckVtsTextEditor as vts

app = QtWidgets.QApplication(sys.argv)  # Crea una aplicacion
form = vts.TextEditorDlg()  # Crea una instancia del formulario
sys.exit(app.exec_())  # Se inicia la aplicacion y se espera eventos
