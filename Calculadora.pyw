# -*- coding: utf-8 -*-

# Base PyQt5

import sys
from math import pi, sin, cos, tan
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

# Cargar nuestro formulario *.ui
form_class = uic.loadUiType("calculadora.ui")[0]


# Crear la Clase MiFormulario con el formulario cargado.
class MiFormulario(QWidget, form_class):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.res = ''

    # Implementacion de los Slots referenciados en QDesigner
    def btpulsado(self):
        boton = self.sender()  # boton tiene la informacion del botón pulsado
        self.res += boton.text()
        self.pantalla.setPlainText(self.res)

    def evalua(self):
        try:
            valor = eval(self.res)
            self.res = '%0.4f' % valor
            self.pantalla.setPlainText(self.res)
        except:
            QMessageBox.information(self, 'error', 'Esta expresion incorrecta')
            self.res = ''
            self.pantalla.setPlainText(self.res)

    def borratodo(self):
        self.res = ''
        self.pantalla.setPlainText(self.res)

    def borra(self):
        self.res = self.res[:-1]
        self.pantalla.setPlainText(self.res)

    def seno(self):
        try:
            valor = sin(eval(self.res) * pi / 180)
            self.res = '%0.4f' % valor
            self.pantalla.setPlainText(self.res)
        except:
            self.res = 'Expresión incorrecta'
            self.pantalla.setPlainText(self.res)

    def coseno(self):
        try:
            valor = cos(eval(self.res) * pi / 180)
            self.res = '%0.4f' % valor
            self.pantalla.setPlainText(self.res)
        except:
            self.res = 'Expresión incorrecta'
            self.pantalla.setPlainText(self.res)

    def tangente(self):
        try:
            valor = tan(eval(self.res) * pi / 180)
            self.res = '%0.4f' % valor
            self.pantalla.setPlainText(self.res)
        except:
            self.res = 'Expresión incorrecta'
            self.pantalla.setPlainText(self.res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MiFormulario(None)
    MyWindow.show()
    app.exec_()
