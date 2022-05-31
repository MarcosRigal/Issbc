#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trabajo Final de Curso ISBC

Aplicación Clasificador

Con este fichero se lanza la aplicación

Authors: Marcos Rivera Gavilan, Marcos Rodriguez Moreno, Moises Moyano Cejudo
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este fichero. El resto que aparezcan sin
comentar, habrán sido comentadas en otros ficheros.
"""

import sys
from PyQt5 import QtWidgets
import ckVtsClasificacion as vts

app = QtWidgets.QApplication(sys.argv)
form = vts.ClasificacionDlg()
sys.exit(app.exec_())
