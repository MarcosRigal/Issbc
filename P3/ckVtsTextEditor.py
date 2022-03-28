"""
Practica 3 ISBC

Applicación Editor de Texto

En este fichero se almacenan las vistas de la aplicación

Author: Marcos Rivera Gavilan
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este ejercicio. El resto que aparezcan sin
comentar, habrán sido comentadas en ejercicios anteriores.
"""

from select import select
import sys
import ckTextEditorController as ctrl

from PyQt5.QtWidgets import QWidget, QTreeView, QFileSystemModel, QApplication, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout


class TextEditorDlg(QWidget):
    def __init__(self):
        super().__init__()
        self.fileName = ["Editor de textos", ".txt"]
        self.initUI()

    def initUI(self):

        self.title = QLabel('Carpeta')
        self.titleEdit = QLineEdit()
        self.titleEdit.setReadOnly(True)
        self.titleEdit.setText("/home/")
        self.selectButton = QPushButton("Seleccionar")

        self.files = QLabel('Archivos')
        self.model = QFileSystemModel()
        self.model.setRootPath("/")
        self.filesEdit = QTreeView()
        self.filesEdit.setModel(self.model)
        self.filesEdit.setRootIndex(self.model.index("/home/"))
        self.filesEdit.clicked.connect(self.on_treeView_clicked)

        self.textEdit = QTextEdit()

        self.saveButton = QPushButton("Guardar")
        self.saveAsButton = QPushButton("Guardar como")

        mainVbox = QVBoxLayout()
        mainVbox.setSpacing(20)

        folderHbox = QHBoxLayout()

        folderHbox.addWidget(self.title)
        folderHbox.addWidget(self.titleEdit)
        folderHbox.addWidget(self.selectButton)

        mainVbox.addLayout(folderHbox)

        grid = QGridLayout()
        grid.setSpacing(10)

        """
        Aquí reamos un diseño de cuadrícula y establecemos
        el espacio entre los distintos elementos
        """

        grid.addWidget(self.files, 0, 0)

        grid.addWidget(self.filesEdit, 1, 0, 1, 2)
        grid.addWidget(self.textEdit, 1, 2, 1, 5)

        grid.addWidget(self.saveButton, 2, 0)
        grid.addWidget(self.saveAsButton, 2, 1)

        mainVbox.addLayout(grid)

        self.setLayout(mainVbox)

        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Review')
        self.show()

        self.selectButton.clicked.connect(self.selectFolder)
        self.saveAsButton.clicked.connect(self.saveAsFile)
        self.saveButton.clicked.connect(self.saveFile)

    def selectFolder(self):
        ctrl.eventSelectFolder(self)

    def on_treeView_clicked(self, index):
        ctrl.eventClickedOnTreeView(self, index)

    def saveAsFile(self):
        ctrl.eventSaveAsFile(self)

    def saveFile(self):
        ctrl.eventSaveFile(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = TextEditorDlg()
    sys.exit(app.exec_())
