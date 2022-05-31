#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trabajo Final de Curso ISBC

Aplicación Clasificador

En este fichero se almacenan el controlador de la aplicación

Authors: Marcos Rivera Gavilan, Marcos Rodriguez Moreno, Moises Moyano Cejudo
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este fichero. El resto que aparezcan sin
comentar, habrán sido comentadas en otros ficheros.
"""

import ckModApClasificacion as ma


def eventGenerar(clasificacionDlg):

    print('ctrl', 'event generar')
    print(ma.mc.clases())


def eventClasificar(clasificacionDlg):
    pass
    print('Objeto:', clasificacionDlg.objeto)
    print('================================\n')
    
    mp = ma.MetodoPoda(clasificacionDlg.objeto)
    r, exp = mp.execute(clasificacionDlg)
    
    clasificacionDlg.plainTextEditExplicacion.clear()
    clasificacionDlg.plainTextEditExplicacion.appendPlainText(exp)

    cs = []

    for cc in r:
        print('         ->', cc.nombre)
        cs.append(cc.nombre)
    
    clasificacionDlg.listWidgetClasesSeleccionadas.clear()
    clasificacionDlg.listWidgetClasesSeleccionadas.addItems(
        cs)

    print('Las clases candidatas: ', r)
    return
