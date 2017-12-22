# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erroresDialog.ui'
#
# Created: Tue Nov 14 13:52:37 2017
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

class Ui_dlg_errores(object):
    def setupUi(self, dlg_errores):
        dlg_errores.setObjectName(_fromUtf8("dlg_errores"))
        dlg_errores.resize(610, 295)
        self.buttonBox = QtGui.QDialogButtonBox(dlg_errores)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tble_covarianza = QtGui.QTableWidget(dlg_errores)
        self.tble_covarianza.setGeometry(QtCore.QRect(40, 31, 231, 171))
        self.tble_covarianza.setObjectName(_fromUtf8("tble_covarianza"))
        self.tble_covarianza.setColumnCount(0)
        self.tble_covarianza.setRowCount(0)
        self.gph_tendencia = QtGui.QGraphicsView(dlg_errores)
        self.gph_tendencia.setGeometry(QtCore.QRect(340, 40, 191, 151))
        self.gph_tendencia.setObjectName(_fromUtf8("gph_tendencia"))

        self.retranslateUi(dlg_errores)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dlg_errores.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dlg_errores.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_errores)

    def retranslateUi(self, dlg_errores):
        dlg_errores.setWindowTitle(_translate("dlg_errores", "Análisis de Errores", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg_errores = QtGui.QDialog()
    ui = Ui_dlg_errores()
    ui.setupUi(dlg_errores)
    dlg_errores.show()
    sys.exit(app.exec_())

