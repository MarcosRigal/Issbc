#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com
"""

from turtle import home
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
from pathlib import Path


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.fileName = ["Editor de textos", ".txt"]
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        saveFile = QAction(QIcon('save.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.saveFile)

        saveAsFile = QAction(QIcon('save.png'), 'Save as', self)
        saveAsFile.setShortcut('F12')
        saveAsFile.setStatusTip('Save As')
        saveAsFile.triggered.connect(self.saveAsFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(saveAsFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle(self.fileName[0])
        self.show()

    def showDialog(self):

        home_dir = str(Path.home())
        self.fileName = QFileDialog.getOpenFileName(
            self, 'Open file', home_dir)

        if self.fileName[0]:
            f = open(self.fileName[0], 'r')
            self.setWindowTitle(self.fileName[0])

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
            self.setWindowTitle(self.fileName[0])

    def saveFile(self):
        if self.fileName == ["Editor de textos", ".txt"]:
            self.saveAsFile()
        else:
            f = open(self.fileName[0], 'w')
            filedata = self.textEdit.toPlainText()
            f.write(filedata)
            f.close()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
