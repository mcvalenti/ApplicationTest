'''
Created on 14 nov. 2017

@author: curso
'''
import sys
from PyQt4 import QtCore, QtGui
from AppTestMain import Ui_MW_AppTest
from cdmWidget import Ui_wgt_CDM
from erroresDialog import Ui_dlg_errores
from printConsola import Ui_Procesamiento
from processingDialog import Ui_Dialog

class AppTest(QtGui.QMainWindow):
    
    def __init__(self):
        super(AppTest,self).__init__()
        
        self.ui = Ui_MW_AppTest()
        self.ui.setupUi(self)
        
        self.ui.btn_cargaCDM.clicked.connect(self.carga_el_CDM)
        self.ui.btn_verProcesamiento.clicked.connect(self.muestra_procesamiento)
    
    def carga_el_CDM(self):
        self.cargaCDM_wgt = CargarCDM()
        self.setCentralWidget(self.cargaCDM_wgt)
        self.cargaCDM_wgt.show()
        
    def muestra_procesamiento(self):
        self.procesamiento_dialog = Procesamiento()
        self.procesamiento_dialog.show()
        
class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))        


class CargarCDM(QtGui.QWidget):
    
    def __init__(self):
        super(CargarCDM,self).__init__()
        
        self.ui = Ui_wgt_CDM()
        self.ui.setupUi(self)
        
        self.ui.btn_analizarErrores.clicked.connect(self.analizar_errores)
        
    def analizar_errores(self):
        self.errores_dialog = AnalisisDeErrores()
        self.errores_dialog.exec_()
        
class AnalisisDeErrores(QtGui.QDialog):
    
    def __init__(self):
        super(AnalisisDeErrores,self).__init__()
        
        self.ui = Ui_dlg_errores()
        self.ui.setupUi(self)
        
class Procesamiento(QtGui.QDialog):
    
    def __init__(self):
        super(Procesamiento,self).__init__()
        
        self.ui = Ui_Procesamiento()
        self.ui.setupUi(self)
        
        self.ui.btn_listar.clicked.connect(self.inicia_procesamiento)
        self.ui.btn_salir.clicked.connect(self.salir)
        self.ui.cbox_directorios.addItems(['perro','gato','caballo','conejo'])
        
#         sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
#     
    def inicia_procesamiento(self):
        for i in range(20):
            print i
        self.proc_dialog = dialogDeProcesamiento()
        self.proc_dialog.exec_()
        

# 
#     def __del__(self):
#         # Restore sys.stdout
#         sys.stdout = sys.__stdout__
#     
#     def normalOutputWritten(self, text):
#         """Append text to the QTextEdit."""
#         # Maybe QTextEdit.append() works as well, but this is how I do it:
#         cursor = self.ui.textEdit.textCursor()
#         cursor.movePosition(QtGui.QTextCursor.End)
#         cursor.insertText(text)
#         self.ui.textEdit.setTextCursor(cursor)
#         self.ui.textEdit.ensureCursorVisible()
  
    def salir(self):
        self.close()

class dialogDeProcesamiento(QtGui.QDialog):
    
    def __init__(self):
        super(dialogDeProcesamiento,self).__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        
    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
     
    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.ui.te_procesando.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.te_procesando.setTextCursor(cursor)
        self.ui.te_procesando.ensureCursorVisible()
  
        
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    w = AppTest()
    w.show()
    sys.exit(app.exec_())