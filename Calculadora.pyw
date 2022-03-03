import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

# Cargar formulario *.ui
form_class = uic.loadUiType("Calculadora.ui")[0]


# crear clase MyWindowClass
class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    # Implementacion de slots
    def mostra(self):
        text = "Texto de prueba para ver que hacemos de nuevo"
        QMessageBox.information(self, 'Botón', text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()
