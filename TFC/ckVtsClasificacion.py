#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trabajo Final de Curso ISBC

Aplicación Clasificador

En este fichero se almacenan las vistas de la aplicación

Authors: Marcos Rivera Gavilan, Marcos Rodriguez Moreno, Moises Moyano Cejudo
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este fichero. El resto que aparezcan sin
comentar, habrán sido comentadas en otros ficheros.
"""

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

import ckCtrlClasificacion as ctrl

lct1 = [[ctrl.ma.mci.Atributo('Marca', 'str', None), 'Mercedes'],
        [ctrl.ma.mci.Atributo('Carroceria', 'str', 'None'), 'Deportivo'],
        [ctrl.ma.mci.Atributo('Plazas', 'int', 'nº'), 2],
        [ctrl.ma.mci.Atributo('Potencia', 'int', 'cv'), 575]]
llct1 = ctrl.ma.mci.creaCaracteristicas(lct1)
ob1 = ctrl.ma.mci.Objeto('ob1', llct1)
ob1.describeObjeto()


lct2 = [[ctrl.ma.mcf.Atributo('Marca', 'str', None), 'YAMAHA'],
        [ctrl.ma.mcf.Atributo('Carroceria', 'str', 'None'), 'Motocross'],
        [ctrl.ma.mcf.Atributo('Tiempos', 'int', 'nº'), 2],
        [ctrl.ma.mcf.Atributo('Potencia', 'int', 'cv'), 25]]

llct2 = ctrl.ma.mcf.creaCaracteristicas(lct2)
ob2 = ctrl.ma.mcf.Objeto('ob2', llct2)
ob2.describeObjeto()


class ClasificacionDlg(QWidget):
    def __init__(self):
        super(ClasificacionDlg, self).__init__()
        self.objeto = ob1

        labelTableWidgetObjeto = QtWidgets.QLabel("Objeto", self)
        labelClasesCandidatas = QtWidgets.QLabel("Clases candidatas", self)
        labelTextDescripcionClases = QtWidgets.QLabel(
            u"Descripción de las clases", self)
        labelListClasesSeleccionadas = QtWidgets.QLabel(
            "Clases seleccionadas", self)
        labelTextjustificacionL = QtWidgets.QLabel(
            u"Justificación de la clasificación", self)
        labelTextjustificacionR = QtWidgets.QLabel(u"", self)

        labelComboxMetodo = QtWidgets.QLabel(u"Método", self)
        labelComboxDominio = QtWidgets.QLabel(u"Dominio", self)

        header = ['ATRIBUTO', 'VALOR']

        self.tableWidgetObjeto = QtWidgets.QTableWidget(4, 2)
        self.tableWidgetObjeto.setColumnWidth(0, 150)
        self.tableWidgetObjeto.setColumnWidth(1, 150)
        self.tableWidgetObjeto.setHorizontalHeaderLabels(header)

        self.listWidgetClasesCandidatas = QtWidgets.QListWidget()

        self.plainTextEditDescripcionClases = QtWidgets.QPlainTextEdit()
        self.listWidgetClasesSeleccionadas = QtWidgets.QListWidget()

        self.plainTextEditExplicacion = QtWidgets.QPlainTextEdit()

        self.comboboxWidgetMetodo = QtWidgets.QComboBox()
        self.comboboxWidgetMetodo.addItem('Poda')

        self.comboboxWidgetDominio = QtWidgets.QComboBox()
        self.comboboxWidgetDominio.addItem('')
        self.comboboxWidgetDominio.addItem('Coches')
        self.comboboxWidgetDominio.addItem('Motos')

        self.clasificarButtom = QtWidgets.QPushButton('Clasificar')
        self.borrarButtom = QtWidgets.QPushButton('Borrar')
        self.salirButtom = QtWidgets.QPushButton('Salir')
        self.buttomsLayout = QtWidgets.QHBoxLayout()
        self.buttomsLayout.addStretch()
        self.buttomsLayout.addWidget(self.clasificarButtom)
        self.buttomsLayout.addWidget(self.borrarButtom)
        self.buttomsLayout.addWidget(self.salirButtom)
        self.buttomsLayout.addStretch()

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelClasesCandidatas, 0, 0)
        grid.addWidget(self.listWidgetClasesCandidatas, 1, 0)
        grid.addWidget(labelTextDescripcionClases, 0, 1)
        grid.addWidget(self.plainTextEditDescripcionClases, 1, 1)
        grid.addWidget(labelTableWidgetObjeto, 0, 2)
        grid.addWidget(self.tableWidgetObjeto, 1, 2)
        grid.addWidget(labelListClasesSeleccionadas, 2, 0)
        grid.addWidget(labelTextjustificacionL, 2, 1)
        grid.addWidget(labelTextjustificacionR, 2, 2)
        grid.addWidget(self.plainTextEditExplicacion, 3, 1, 6, 2)
        grid.addWidget(self.listWidgetClasesSeleccionadas, 3, 0)
        grid.addWidget(labelComboxDominio, 4, 0)
        grid.addWidget(self.comboboxWidgetDominio, 5, 0)
        grid.addWidget(labelComboxMetodo, 6, 0)
        grid.addWidget(self.comboboxWidgetMetodo, 7, 0)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttomsLayout)
        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 1005, 545)
        self.setWindowTitle(u"Trabajo Final de Curso")
        self.show()
        self.center()

        self.listWidgetClasesCandidatas.itemClicked.connect(self.showCc)
        self.tableWidgetObjeto.itemChanged.connect(self.changeObj)
        self.clasificarButtom.clicked.connect(self.clasificar)
        self.salirButtom.clicked.connect(self.close)
        self.comboboxWidgetDominio.currentIndexChanged.connect(
            self.changeCandidateClases)

    def changeCandidateClases(self):

        self.listWidgetClasesCandidatas.clear()
        emptyItem = QtWidgets.QTableWidgetItem("")

        for i in range(4):
            self.tableWidgetObjeto.setItem(i, 0, emptyItem)
            self.tableWidgetObjeto.setItem(i, 1, emptyItem)

        if self.comboboxWidgetDominio.currentText() == 'Coches':

            self.objeto = ob1
            self.cc = ctrl.ma.mci.clases()

            if self.cc is not None:
                pass

                stringList = []

                for c in self.cc:
                    stringList.append(c.nombre)

                self.listWidgetClasesCandidatas.addItems(stringList)
                self.listWidgetClasesCandidatas.setCurrentRow(0)

            i = 0

            for at in ob1.caracteristicas:
                print(at)
                print(at.atributo.nombre, at.atributo.tipo,
                      at.valor, type(at.valor), at.atributo.unidad)

                item1 = QtWidgets.QTableWidgetItem(at.atributo.nombre)
                item1.setFlags(QtCore.Qt.ItemIsUserCheckable |
                               QtCore.Qt.ItemIsEnabled)

                if at.atributo.tipo == 'multiple':
                    combobox = QtWidgets.QComboBox()

                elif at.atributo.tipo == 'boleano':
                    combobox = QtWidgets.QComboBox()
                    combobox.addItem('True')
                    combobox.addItem('False')
                    self.tableWidgetPosiblesFallos.setCellWidget(
                        i, 1, combobox)
                self.tableWidgetObjeto.setItem(i, 0, item1)
                if isinstance(at.valor, int):
                    item2 = QtWidgets.QTableWidgetItem(str(at.valor))
                elif isinstance(at.valor, str):
                    item2 = QtWidgets.QTableWidgetItem(at.valor)
                self.tableWidgetObjeto.setItem(i, 1, item2)
                i += 1
                self.changeObj
        else:
            self.objeto = ob2
            self.cc = ctrl.ma.mcf.clases()
            if self.cc is not None:
                pass
                stringList = []
                for c in self.cc:
                    stringList.append(c.nombre)
                self.listWidgetClasesCandidatas.addItems(stringList)
                self.listWidgetClasesCandidatas.setCurrentRow(0)
            i = 0
            for at in ob2.caracteristicas:
                print(at)
                print(at.atributo.nombre, at.atributo.tipo,
                      at.valor, type(at.valor), at.atributo.unidad)

                item1 = QtWidgets.QTableWidgetItem(at.atributo.nombre)
                item1.setFlags(QtCore.Qt.ItemIsUserCheckable |
                               QtCore.Qt.ItemIsEnabled)

                if at.atributo.tipo == 'multiple':
                    combobox = QtWidgets.QComboBox()

                elif at.atributo.tipo == 'boleano':
                    combobox = QtWidgets.QComboBox()
                    combobox.addItem('True')
                    combobox.addItem('False')
                    self.tableWidgetPosiblesFallos.setCellWidget(
                        i, 1, combobox)
                self.tableWidgetObjeto.setItem(i, 0, item1)
                if isinstance(at.valor, int):
                    item2 = QtWidgets.QTableWidgetItem(str(at.valor))
                elif isinstance(at.valor, str):
                    item2 = QtWidgets.QTableWidgetItem(at.valor)
                self.tableWidgetObjeto.setItem(i, 1, item2)
                i += 1
                self.changeObj

    def generar(self):
        print('generar')
        ctrl.eventGenerar(self)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showCc(self):
        row = self.listWidgetClasesCandidatas.currentRow()
        self.plainTextEditDescripcionClases.clear()
        self.plainTextEditDescripcionClases.appendPlainText(
            self.cc[row].descripcion())
        pass

    def changeObj(self):
        print('Objeto cambiado')
        for i in range(self.tableWidgetObjeto.rowCount()):
            item1 = self.tableWidgetObjeto.item(i, 0)
            item2 = self.tableWidgetObjeto.item(i, 1)
            if self.objeto.caracteristicas[i].atributo.tipo == 'str':
                self.objeto.caracteristicas[i].valor = self.tableWidgetObjeto.item(
                    i, 1).text()
            elif self.objeto.caracteristicas[i].atributo.tipo == 'int':
                print('---->', self.tableWidgetObjeto.item(i, 1).text())
                self.objeto.caracteristicas[i].valor = int(
                    self.tableWidgetObjeto.item(i, 1).text())

        for at in self.objeto.caracteristicas:
            print(at.atributo.nombre, at.valor)
            pass

    def clasificar(self):
        print('clasificar')
        ctrl.eventClasificar(self)
