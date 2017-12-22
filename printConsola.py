# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printConsola.ui'
#
# Created: Fri Dec 22 09:05:10 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Procesamiento(object):
    def setupUi(self, Procesamiento):
        Procesamiento.setObjectName(_fromUtf8("Procesamiento"))
        Procesamiento.resize(674, 452)
        self.btn_salir = QtGui.QPushButton(Procesamiento)
        self.btn_salir.setGeometry(QtCore.QRect(480, 210, 96, 31))
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.gbox_seleccion_archivos = QtGui.QGroupBox(Procesamiento)
        self.gbox_seleccion_archivos.setGeometry(QtCore.QRect(40, 50, 571, 171))
        self.gbox_seleccion_archivos.setObjectName(_fromUtf8("gbox_seleccion_archivos"))
        self.lb_selec_dir = QtGui.QLabel(self.gbox_seleccion_archivos)
        self.lb_selec_dir.setGeometry(QtCore.QRect(10, 40, 201, 21))
        self.lb_selec_dir.setObjectName(_fromUtf8("lb_selec_dir"))
        self.cbox_directorios = QtGui.QComboBox(self.gbox_seleccion_archivos)
        self.cbox_directorios.setGeometry(QtCore.QRect(10, 80, 381, 51))
        self.cbox_directorios.setObjectName(_fromUtf8("cbox_directorios"))
        self.btn_listar = QtGui.QPushButton(self.gbox_seleccion_archivos)
        self.btn_listar.setGeometry(QtCore.QRect(420, 80, 111, 31))
        self.btn_listar.setObjectName(_fromUtf8("btn_listar"))
        self.textEdit = QtGui.QTextEdit(Procesamiento)
        self.textEdit.setGeometry(QtCore.QRect(50, 220, 291, 181))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Procesamiento)
        QtCore.QMetaObject.connectSlotsByName(Procesamiento)

    def retranslateUi(self, Procesamiento):
        Procesamiento.setWindowTitle(_translate("Procesamiento", "Form", None))
        self.btn_salir.setText(_translate("Procesamiento", "Salir", None))
        self.gbox_seleccion_archivos.setTitle(_translate("Procesamiento", "Seleccion de Archivos", None))
        self.lb_selec_dir.setText(_translate("Procesamiento", "Seleccione el directorio", None))
        self.btn_listar.setText(_translate("Procesamiento", "Listar Archivos", None))

