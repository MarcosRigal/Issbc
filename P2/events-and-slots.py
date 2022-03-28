from select import select
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QFileDialog, QPushButton, QGridLayout, QFileSystemModel, QTreeView
from pathlib import Path


class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.fileName = ["Editor de textos", ".txt"]
        self.initUI()

    def initUI(self):

        self.model = QFileSystemModel()
        self.model.setRootPath("/")
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index("/home/"))
        self.tree.clicked.connect(self.on_treeView_clicked)

        self.title = QLabel('Carpeta')
        self.titleEdit = QLineEdit()
        self.titleEdit.setReadOnly(True)
        self.titleEdit.setText("/home/")

        self.files = QLabel('Archivos')
        self.filesEdit = QTextEdit()

        self.textEdit = QTextEdit()

        self.selectButton = QPushButton("Carpeta")
        self.selectButton.clicked.connect(self.selectDialog)
        self.openButton = QPushButton("Abrir")
        self.openButton.clicked.connect(self.showDialog)
        self.saveButton = QPushButton("Guardar")
        self.saveButton.clicked.connect(self.saveFile)
        self.saveAsButton = QPushButton("Guardar como")
        self.saveAsButton.clicked.connect(self.saveAsFile)
        self.closeButton = QPushButton("Cerrar")
        self.closeButton.clicked.connect(self.close)
        self.exitButton = QPushButton("Exit")
        self.exitButton.clicked.connect(QApplication.instance().quit)

        mainVbox = QVBoxLayout()
        mainVbox.setSpacing(20)

        grid = QGridLayout()
        grid.setSpacing(10)

        """
        Aquí reamos un diseño de cuadrícula y establecemos
        el espacio entre los distintos elementos
        """

        grid.addWidget(self.title, 0, 0)
        grid.addWidget(self.titleEdit, 0, 1, 1, 5)
        grid.addWidget(self.selectButton, 0, 6)

        grid.addWidget(self.files, 1, 0)
        grid.addWidget(self.openButton, 1, 6)

        grid.addWidget(self.tree, 2, 0, 5, 2)
        grid.addWidget(self.textEdit, 2, 2, 5, 4)
        grid.addWidget(self.saveButton, 2, 6)

        grid.addWidget(self.saveAsButton, 3, 6)
        grid.addWidget(self.closeButton, 4, 6)
        grid.addWidget(self.exitButton, 5, 6)

        self.setLayout(grid)

        self.setGeometry(500, 500, 900, 500)
        self.setWindowTitle('Review')
        self.show()

    def selectDialog(self):
        home_dir = str(Path.home())
        self.fileName = QFileDialog.getExistingDirectory(
            self, 'Open file', home_dir)

        if self.fileName:
            self.titleEdit.setText(self.fileName)
            self.tree.setRootIndex(self.model.index(self.fileName))

    def showDialog(self):
        home_dir = str(Path.home())
        self.fileName = QFileDialog.getOpenFileName(
            self, 'Open file', home_dir)

        if self.fileName[0]:
            f = open(self.fileName[0], 'r')
            self.titleEdit.setText(self.fileName[0])

            with f:
                data = f.read()
                self.textEdit.setText(data)

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
            self.saveAsFile()
        else:
            f = open(self.fileName[0], 'w')
            filedata = self.textEdit.toPlainText()
            f.write(filedata)
            f.close()

    def close(self):
        self.textEdit.setText("")
        self.fileName[0] = ""
        self.titleEdit.setText(self.fileName[0])

    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        fileName = self.model.fileName(indexItem)
        self.fileName[0] = self.model.filePath(indexItem)
        self.titleEdit.setText(self.fileName[0])

        f = open(self.fileName[0], 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = TextEditor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
