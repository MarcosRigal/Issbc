#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:29:53 2014

@author: acalvo
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

import ckCtrlClasificacion as ctrl

import mcIris as mc    #Cambiar al cambiar el MC ver en main
#import mcFrutos as mc #ver en main

lct1=[[ctrl.ma.mc.Atributo('Ancho sepalo','int','mm'),25],
       [ctrl.ma.mc.Atributo('Largo sepalo','int','mm'),110],
       [ctrl.ma.mc.Atributo('Ancho petalo','int','mm'),30],
       [ctrl.ma.mc.Atributo('Largo petalo','int','mm'),95]]
llct1=ctrl.ma.mc.creaCaracteristicas(lct1)
ob1=ctrl.ma.mc.Objeto('ob1',llct1)
ob1.describeObjeto()


lct=[[ctrl.ma.mc.Atributo('diametro','int','cm'),180],
     [ctrl.ma.mc.Atributo('peso','int','gr'),8000],
     [ctrl.ma.mc.Atributo('color','str',None),'verde']]


llct=ctrl.ma.mc.creaCaracteristicas(lct)
ob2=ctrl.ma.mc.Objeto('ob2',llct)

ob=ob2
ob.describeObjeto()



class ClasificacionDlg(QWidget):
    def __init__(self):
        super(ClasificacionDlg, self).__init__()
        self.objeto=ob1 
        #Label
        labelTableWidgetObjeto=QtWidgets.QLabel("Objeto",self)  
        labelClasesCandidatas=QtWidgets.QLabel("Clases candidatas",self)
        labelTextDescripcionClases=QtWidgets.QLabel(u"Descripci�n de las clases",self)        
        labelListClasesSeleccionadas=QtWidgets.QLabel("Clases seleccionadas",self)
        labelTextjustificacionL=QtWidgets.QLabel(u"Justificaci�n de la clasificaci�n",self)
        labelTextjustificacionR=QtWidgets.QLabel(u"",self)
        
        labelComboxMetodo=QtWidgets.QLabel(u"M�todo",self)
        labelComboxDominio=QtWidgets.QLabel(u"Dominio",self)
        
        #Widget
        header = ['ATRIBUTO', 'VALOR']
        #posiblesFallos = Fallos(self,   observables_list, header)
        self.tableWidgetObjeto = QtWidgets.QTableWidget(len(ob1.caracteristicas),2) #Crea la tabla de elementos observables de dos columnas
        self.tableWidgetObjeto.setColumnWidth(0, 140) #Asignan ancho a las columnas
        self.tableWidgetObjeto.setColumnWidth(1, 200) #Asignan ancho a las columnas
        self.tableWidgetObjeto.setHorizontalHeaderLabels(header) #Asigna etiquetas a las columnas
        #print observables
        i=0
        for at in ob1.caracteristicas:
            print (at)
            print  (at.atributo.nombre,at.atributo.tipo, at.valor,type(at.valor),at.atributo.unidad)#,
            item1 = QtWidgets.QTableWidgetItem(at.atributo.nombre) #Crea un item y le asigna el nombre de la observable
            #item1.setCheckState(QtCore.Qt.Checked) # Establece propiedades a las celdas de la primera columna de la tabla
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna

            if at.atributo.tipo=='multiple':#Si el tipo de observable es m�ltiple creamos un combox
                combobox = QtWidgets.QComboBox()
                #for j in observables[i].valoresPermitidos:#a�adimmos al combox los valeores permitidos
                 #   combobox.addItem(j) 
                #self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)#Establecemos en la celda i el combox
            elif at.atributo.tipo=='boleano':#Si es boleano creamos otro combox con dos posibles valores
                combobox = QtWidgets.QComboBox()
                combobox.addItem('True') 
                combobox.addItem('False') 
                self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)
            self.tableWidgetObjeto.setItem(i, 0, item1)#Establecemos el item en la columna 0
            if  isinstance(at.valor,int):
                item2 = QtWidgets.QTableWidgetItem(str(at.valor))
            elif  isinstance(at.valor,str):
                item2 = QtWidgets.QTableWidgetItem(at.valor)
            self.tableWidgetObjeto.setItem(i, 1, item2)#Establecemos el item en la columna 0
            i+=1
        
        #List
        self.listWidgetClasesCandidatas = QtWidgets.QListWidget()
        self.cc=ctrl.ma.mc.clases()
        if self.cc is not None:
            pass
            stringList=[]
            for c in self.cc:
                stringList.append(c.nombre)
                
            self.listWidgetClasesCandidatas.addItems(stringList)
            self.listWidgetClasesCandidatas.setCurrentRow(0)
    
        self.plainTextEditDescripcionClases = QtWidgets.QPlainTextEdit()#Cuadro de texto de descripcion de la clase
        self.listWidgetClasesSeleccionadas = QtWidgets.QListWidget()
        self.plainTextEditExplicacion = QtWidgets.QPlainTextEdit()#Cuadro de texto    de la explicaci�n
        
        #M�todo
        self.comboboxWidgetMetodo = QtWidgets.QComboBox()
        self.comboboxWidgetMetodo.addItem('Poda')
        self.comboboxWidgetMetodo.addItem('Semi Poda') 

        #Dominio
        self.comboboxWidgetDominio = QtWidgets.QComboBox()
        self.comboboxWidgetDominio.addItem('Frutos')
        self.comboboxWidgetDominio.addItem('Iris') 
        
        #Botones
        self.clasificarButtom=QtWidgets.QPushButton('Clasificar')
        self.borrarButtom=QtWidgets.QPushButton('Borrar')
        self.salirButtom=QtWidgets.QPushButton('Salir') 
        self.buttomsLayout = QtWidgets.QHBoxLayout()
        self.buttomsLayout.addStretch()
        self.buttomsLayout.addWidget(self.clasificarButtom)
        self.buttomsLayout.addWidget(self.borrarButtom)
        self.buttomsLayout.addWidget(self.salirButtom)
        self.buttomsLayout.addStretch()
        
        #Rejilla de distribuci�n de los controles
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
        grid.addWidget(self.plainTextEditExplicacion, 3, 1,6,2)
        grid.addWidget(self.listWidgetClasesSeleccionadas, 3, 0)
        grid.addWidget(labelComboxDominio, 4, 0)
        grid.addWidget(self.comboboxWidgetDominio, 5, 0)
        grid.addWidget(labelComboxMetodo, 6, 0)
        grid.addWidget(self.comboboxWidgetMetodo, 7, 0)   
        
        
        
        
        #Dise�o principal
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttomsLayout)
        self.setLayout(mainLayout)
        
    
        self.setGeometry(300, 300, 1123, 800)
        self.setWindowTitle(u"TAREA DE CLASIFICACION")
        self.show()
 
        self.center()
        #Conexiones:
        #==========
        self.listWidgetClasesCandidatas.itemClicked.connect(self.showCc)
        self.tableWidgetObjeto.itemChanged.connect(self.changeObj)
        #self.generarButtom.clicked.connect(self.generar)
        self.clasificarButtom.clicked.connect(self.clasificar)
        self.salirButtom.clicked.connect(self.close)
        self.comboboxWidgetDominio.currentIndexChanged.connect(self.hola)

    def hola(self):
        print(self.comboboxWidgetDominio.currentText())

    def generar(self):
        print ('generar')
        ctrl.eventGenerar(self)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showCc(self):
        row = self.listWidgetClasesCandidatas.currentRow()
        #print row
        #print self.cc[row].nombre
        #print self.cc[row].descripcion()
        self.plainTextEditDescripcionClases.clear()
        self.plainTextEditDescripcionClases.appendPlainText(self.cc[row].descripcion())
        pass
    
    def changeObj(self):
        '''
        Cambia los valores del objeto tomando los datos de la tabla.
        '''
        print ('objeto cambiado')
        for i in range(self.tableWidgetObjeto.rowCount()):
        #print i
            item1=self.tableWidgetObjeto.item(i,0)
            item2=self.tableWidgetObjeto.item(i,1)
            #print item1, item1.text(),self.objeto.caracteristicas[i].atributo.nombre,self.objeto.caracteristicas[i].valor
            #print item2, item2.text()
            if self.objeto.caracteristicas[i].atributo.tipo=='str':
                self.objeto.caracteristicas[i].valor=self.tableWidgetObjeto.item(i,1).text()
            elif self.objeto.caracteristicas[i].atributo.tipo=='int':
                print ('---->',self.tableWidgetObjeto.item(i,1).text())
                self.objeto.caracteristicas[i].valor=int(self.tableWidgetObjeto.item(i,1).text())

        for at in self.objeto.caracteristicas:
            print (at.atributo.nombre, at.valor)
            pass
    
    def clasificar(self):
        print ('clasificar')
        ctrl.eventClasificar(self)
    



if __name__ == "__main__":
    import mcFrutos as mc #Cambiar al cambiar el MC
    #import mcIris as mc #Cambiar al cambiar el MC
   
    lct1=[[mc.Atributo('diametro','int','cm'),180],[mc.Atributo('peso','int','gr'),6000],[mc.Atributo('color','str',None),'verde']]
    llct1=mc.creaCaracteristicas(lct1)
    ob2=mc.Objeto('ob2',llct1)
    ob2.describeObjeto()


    
    lct=[[mc.Atributo('Ancho sepalo','int','mm'),25],[mc.Atributo('Largo sepalo','int','mm'),110],[mc.Atributo('Ancho petalo','int','mm'),30],
                  [mc.Atributo('Largo petalo','int','mm'),95]]
    llct=mc.creaCaracteristicas(lct)
    ob1=mc.Objeto('ob1',llct)#creo el objeto
    
    ob=ob2  #Se crea el objeto con el que vamos a trabajar
    print (ob)
    ob.describeObjeto()
    app = QtWidgets.QApplication(sys.argv)
    form = ClasificacionDlg(ob)
    sys.exit(app.exec_())


 