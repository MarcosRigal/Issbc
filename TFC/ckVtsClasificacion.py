#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

import ckCtrlClasificacion as ctrl

import mcIris as mci  # Cambiar al cambiar el MC ver en main
import mcFrutos as mcf  # ver en main

lct1 = [[ctrl.ma.mci.Atributo('Ancho sepalo', 'int', 'mm'), 25],
        [ctrl.ma.mci.Atributo('Largo sepalo', 'int', 'mm'), 110],
        [ctrl.ma.mci.Atributo('Ancho petalo', 'int', 'mm'), 30],
        [ctrl.ma.mci.Atributo('Largo petalo', 'int', 'mm'), 95]]
llct1 = ctrl.ma.mci.creaCaracteristicas(lct1)
ob1 = ctrl.ma.mci.Objeto('ob1', llct1)
ob1.describeObjeto()


lct = [[ctrl.ma.mcf.Atributo('diametro', 'int', 'cm'), 180],
       [ctrl.ma.mcf.Atributo('peso', 'int', 'gr'), 8000],
       [ctrl.ma.mcf.Atributo('color', 'str', None), 'verde']]

llct = ctrl.ma.mcf.creaCaracteristicas(lct)
ob2 = ctrl.ma.mcf.Objeto('ob2', llct)

ob = ob2
ob.describeObjeto()


class ClasificacionDlg(QWidget):
    def __init__(self):
        super(ClasificacionDlg, self).__init__()
        self.objeto = ob1
        # Label
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

        # Widget
        header = ['ATRIBUTO', 'VALOR']
        #posiblesFallos = Fallos(self,   observables_list, header)
        # Crea la tabla de elementos observables de dos columnas
        self.tableWidgetObjeto = QtWidgets.QTableWidget(
            len(ob1.caracteristicas), 2)
        self.tableWidgetObjeto.setColumnWidth(
            0, 140)  # Asignan ancho a las columnas
        self.tableWidgetObjeto.setColumnWidth(
            1, 200)  # Asignan ancho a las columnas
        self.tableWidgetObjeto.setHorizontalHeaderLabels(
            header)  # Asigna etiquetas a las columnas
        # print observables
        i = 0
        for at in ob1.caracteristicas:
            print(at)
            print(at.atributo.nombre, at.atributo.tipo, at.valor,
                  type(at.valor), at.atributo.unidad)  # ,
            # Crea un item y le asigna el nombre de la observable
            item1 = QtWidgets.QTableWidgetItem(at.atributo.nombre)
            # item1.setCheckState(QtCore.Qt.Checked) # Establece propiedades a las celdas de la primera columna de la tabla
            # Establece propiedades a las celdas de la primera columna
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable |
                           QtCore.Qt.ItemIsEnabled)

            if at.atributo.tipo == 'multiple':  # Si el tipo de observable es m�ltiple creamos un combox
                combobox = QtWidgets.QComboBox()
                # for j in observables[i].valoresPermitidos:#a�adimmos al combox los valeores permitidos
                #   combobox.addItem(j)
                # self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)#Establecemos en la celda i el combox
            elif at.atributo.tipo == 'boleano':  # Si es boleano creamos otro combox con dos posibles valores
                combobox = QtWidgets.QComboBox()
                combobox.addItem('True')
                combobox.addItem('False')
                self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)
            # Establecemos el item en la columna 0
            self.tableWidgetObjeto.setItem(i, 0, item1)
            if isinstance(at.valor, int):
                item2 = QtWidgets.QTableWidgetItem(str(at.valor))
            elif isinstance(at.valor, str):
                item2 = QtWidgets.QTableWidgetItem(at.valor)
            # Establecemos el item en la columna 0
            self.tableWidgetObjeto.setItem(i, 1, item2)
            i += 1

        # List
        self.listWidgetClasesCandidatas = QtWidgets.QListWidget()

        # Cuadro de texto de descripcion de la clase
        self.plainTextEditDescripcionClases = QtWidgets.QPlainTextEdit()
        self.listWidgetClasesSeleccionadas = QtWidgets.QListWidget()
        # Cuadro de texto    de la explicaci�n
        self.plainTextEditExplicacion = QtWidgets.QPlainTextEdit()

        # M�todo
        self.comboboxWidgetMetodo = QtWidgets.QComboBox()
        self.comboboxWidgetMetodo.addItem('')
        self.comboboxWidgetMetodo.addItem('Poda')
        self.comboboxWidgetMetodo.addItem('Semi Poda')

        # Dominio
        self.comboboxWidgetDominio = QtWidgets.QComboBox()
        self.comboboxWidgetDominio.addItem('')
        self.comboboxWidgetDominio.addItem('Frutos')
        self.comboboxWidgetDominio.addItem('Iris')

        # Botones
        self.clasificarButtom = QtWidgets.QPushButton('Clasificar')
        self.borrarButtom = QtWidgets.QPushButton('Borrar')
        self.salirButtom = QtWidgets.QPushButton('Salir')
        self.buttomsLayout = QtWidgets.QHBoxLayout()
        self.buttomsLayout.addStretch()
        self.buttomsLayout.addWidget(self.clasificarButtom)
        self.buttomsLayout.addWidget(self.borrarButtom)
        self.buttomsLayout.addWidget(self.salirButtom)
        self.buttomsLayout.addStretch()

        # Rejilla de distribuci�n de los controles
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

        # Dise�o principal
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttomsLayout)
        self.setLayout(mainLayout)

        self.setGeometry(300, 300, 1125, 800)
        self.setWindowTitle(u"Trabajo Final de Curso")
        self.show()

        self.center()
        # Conexiones:
        self.listWidgetClasesCandidatas.itemClicked.connect(self.showCc)
        self.tableWidgetObjeto.itemChanged.connect(self.changeObj)
        self.clasificarButtom.clicked.connect(self.clasificar)
        self.salirButtom.clicked.connect(self.close)
        self.comboboxWidgetDominio.currentIndexChanged.connect(
            self.changeCandidateClases)

    def changeCandidateClases(self):
        self.listWidgetClasesCandidatas.clear()
        if self.comboboxWidgetDominio.currentText() == 'Iris':
            self.cc = ctrl.ma.mci.clases()
            if self.cc is not None:
                pass
                stringList = []
                for c in self.cc:
                    stringList.append(c.nombre)
                self.listWidgetClasesCandidatas.addItems(stringList)
                self.listWidgetClasesCandidatas.setCurrentRow(0)
        else:
            self.cc = ctrl.ma.mcf.clases()
            if self.cc is not None:
                pass
                stringList = []
                for c in self.cc:
                    stringList.append(c.nombre)
                self.listWidgetClasesCandidatas.addItems(stringList)
                self.listWidgetClasesCandidatas.setCurrentRow(0)

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
        # print row
        # print self.cc[row].nombre
        # print self.cc[row].descripcion()
        self.plainTextEditDescripcionClases.clear()
        self.plainTextEditDescripcionClases.appendPlainText(
            self.cc[row].descripcion())
        pass

    def changeObj(self):
        '''
        Cambia los valores del objeto tomando los datos de la tabla.
        '''
        print('objeto cambiado')
        for i in range(self.tableWidgetObjeto.rowCount()):
            # print i
            item1 = self.tableWidgetObjeto.item(i, 0)
            item2 = self.tableWidgetObjeto.item(i, 1)
            # print item1, item1.text(),self.objeto.caracteristicas[i].atributo.nombre,self.objeto.caracteristicas[i].valor
            # print item2, item2.text()
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


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    form = ClasificacionDlg()
    sys.exit(app.exec_())
