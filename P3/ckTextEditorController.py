"""
Practica 3 ISBC

Applicación Editor de Texto

En este fichero se encuentra el controlador encargado
de relacionar la vista con el modelo

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""
import ckModAppTextEditor as mapp


def eventSelectFolder(self):
    file = mapp.selectFolder(self)
    return file