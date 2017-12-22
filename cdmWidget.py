# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cdmWidget.ui'
#
# Created: Tue Nov 14 13:44:15 2017
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

class Ui_wgt_CDM(object):
    def setupUi(self, wgt_CDM):
        wgt_CDM.setObjectName(_fromUtf8("wgt_CDM"))
        wgt_CDM.resize(662, 299)
        self.gbox_cdmMetaData = QtGui.QGroupBox(wgt_CDM)
        self.gbox_cdmMetaData.setGeometry(QtCore.QRect(30, 20, 571, 201))
        self.gbox_cdmMetaData.setObjectName(_fromUtf8("gbox_cdmMetaData"))
        self.lab_noradSat = QtGui.QLabel(self.gbox_cdmMetaData)
        self.lab_noradSat.setGeometry(QtCore.QRect(80, 30, 141, 21))
        self.lab_noradSat.setObjectName(_fromUtf8("lab_noradSat"))
        self.le_noradSat = QtGui.QLineEdit(self.gbox_cdmMetaData)
        self.le_noradSat.setGeometry(QtCore.QRect(220, 30, 171, 31))
        self.le_noradSat.setObjectName(_fromUtf8("le_noradSat"))
        self.lab_noradDeb = QtGui.QLabel(self.gbox_cdmMetaData)
        self.lab_noradDeb.setGeometry(QtCore.QRect(80, 70, 111, 21))
        self.lab_noradDeb.setObjectName(_fromUtf8("lab_noradDeb"))
        self.le_noradDeb = QtGui.QLineEdit(self.gbox_cdmMetaData)
        self.le_noradDeb.setGeometry(QtCore.QRect(220, 70, 171, 31))
        self.le_noradDeb.setObjectName(_fromUtf8("le_noradDeb"))
        self.lab_TCA = QtGui.QLabel(self.gbox_cdmMetaData)
        self.lab_TCA.setGeometry(QtCore.QRect(110, 120, 65, 21))
        self.lab_TCA.setObjectName(_fromUtf8("lab_TCA"))
        self.btn_calcular = QtGui.QPushButton(self.gbox_cdmMetaData)
        self.btn_calcular.setGeometry(QtCore.QRect(450, 160, 96, 31))
        self.btn_calcular.setObjectName(_fromUtf8("btn_calcular"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.gbox_cdmMetaData)
        self.dateTimeEdit.setGeometry(QtCore.QRect(220, 110, 194, 33))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.btn_analizarErrores = QtGui.QPushButton(wgt_CDM)
        self.btn_analizarErrores.setGeometry(QtCore.QRect(490, 230, 131, 31))
        self.btn_analizarErrores.setObjectName(_fromUtf8("btn_analizarErrores"))

        self.retranslateUi(wgt_CDM)
        QtCore.QMetaObject.connectSlotsByName(wgt_CDM)

    def retranslateUi(self, wgt_CDM):
        wgt_CDM.setWindowTitle(_translate("wgt_CDM", "CDM", None))
        self.gbox_cdmMetaData.setTitle(_translate("wgt_CDM", "Informacion Principal", None))
        self.lab_noradSat.setText(_translate("wgt_CDM", "NORAD Satelite", None))
        self.lab_noradDeb.setText(_translate("wgt_CDM", "NORAD Desecho", None))
        self.lab_TCA.setText(_translate("wgt_CDM", "TCA", None))
        self.btn_calcular.setText(_translate("wgt_CDM", "CALCULAR", None))
        self.btn_analizarErrores.setText(_translate("wgt_CDM", "Analizar Errores", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    wgt_CDM = QtGui.QWidget()
    ui = Ui_wgt_CDM()
    ui.setupUi(wgt_CDM)
    wgt_CDM.show()
    sys.exit(app.exec_())

