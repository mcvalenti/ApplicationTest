# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppTest.ui'
#
# Created: Thu Dec 21 14:12:35 2017
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

class Ui_MW_AppTest(object):
    def setupUi(self, MW_AppTest):
        MW_AppTest.setObjectName(_fromUtf8("MW_AppTest"))
        MW_AppTest.resize(734, 523)
        self.centralwidget = QtGui.QWidget(MW_AppTest)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 90, 351, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_cargaCDM = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_cargaCDM.setObjectName(_fromUtf8("btn_cargaCDM"))
        self.verticalLayout.addWidget(self.btn_cargaCDM)
        self.btn_cargaManual = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_cargaManual.setObjectName(_fromUtf8("btn_cargaManual"))
        self.verticalLayout.addWidget(self.btn_cargaManual)
        self.btn_verProcesamiento = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_verProcesamiento.setObjectName(_fromUtf8("btn_verProcesamiento"))
        self.verticalLayout.addWidget(self.btn_verProcesamiento)
        MW_AppTest.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MW_AppTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MW_AppTest.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MW_AppTest)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MW_AppTest.setStatusBar(self.statusbar)

        self.retranslateUi(MW_AppTest)
        QtCore.QMetaObject.connectSlotsByName(MW_AppTest)

    def retranslateUi(self, MW_AppTest):
        MW_AppTest.setWindowTitle(_translate("MW_AppTest", "Application Test", None))
        self.btn_cargaCDM.setText(_translate("MW_AppTest", "Cargar CDM", None))
        self.btn_cargaManual.setText(_translate("MW_AppTest", "Carga Manual", None))
        self.btn_verProcesamiento.setText(_translate("MW_AppTest", "Ver Procesamiento", None))

