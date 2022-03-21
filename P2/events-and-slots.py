from select import select
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QFileSystemModel, QTreeView


class TextEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.model = QFileSystemModel()
        self.model.setRootPath("/")
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index("/"))
        self.tree.clicked.connect(self.on_treeView_clicked)

        self.title = QLabel('Carpeta')
        self.titleEdit = QLineEdit()

        self.files = QLabel('Archivos')
        self.filesEdit = QTextEdit()

        self.textEdit = QTextEdit()

        self.selectButton = QPushButton("Carpeta")
        self.openButton = QPushButton("Abrir")
        self.saveButton = QPushButton("Guardar")
        self.saveAsButton = QPushButton("Guardar como")
        self.closeButton = QPushButton("Cerrar")
        self.exitButton = QPushButton("Exit")

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

        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Review')
        self.show()

    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        f = open(filePath, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = TextEditor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
