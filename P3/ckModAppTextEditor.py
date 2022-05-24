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
    self.fileName[0] = QFileDialog.getExistingDirectory(
        self, 'Open file', home_dir)
    print(self.fileName[0])
    if self.fileName[0]:
        self.titleEdit.setText(self.fileName[0])
        self.filesEdit.setRootIndex(self.model.index(self.fileName[0]))


def saveAsFile(self):
    home_dir = str(Path.home())
    name = QFileDialog.getSaveFileName(
        self, 'Save File', home_dir)
    print(name)
    if len(name[0]):
        self.fileName = name
        f = open(self.fileName[0], 'w')
        filedata = self.textEdit.toPlainText()
        f.write(filedata)
        f.close()
        self.titleEdit.setText(self.fileName[0])


def saveFile(self):
    if self.fileName == ["Editor de textos", ".txt"]:
        self.saveAsFile(self)
    else:
        f = open(self.fileName[0], 'w')
        filedata = self.textEdit.toPlainText()
        f.write(filedata)
        f.close()


def on_treeView_clicked(self, index):
    indexItem = self.model.index(index.row(), 0, index.parent())

    fileName = self.model.fileName(indexItem)
    self.fileName[0] = self.model.filePath(indexItem)
    self.titleEdit.setText(self.fileName[0])

    f = open(self.fileName[0], 'r')

    with f:
        data = f.read()
        self.textEdit.setText(data)
