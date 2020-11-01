"""
Carlos Paredes Márquez.
Importar window a code. xd
28/10/2020.
"""
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox #use de clase QFileDialog
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from libreria import Libreria
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
    
        self.libreria = Libreria()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
    
    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.libreria.abrir(ubicacion):
            QMessageBox.information(
                self,
                'Éxito',
                'Se abrio el archivo ' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                'Error',
                'Error al abrir el archivo ' + ubicacion
            )
    
    @Slot() #Hacer uso de la biblioteca json
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar como',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.libreria.guardar(ubicacion):
            QMessageBox.information(
                self,
                'Éxito',
                'Se pudo crear el archivo ' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo crear el archivo ' + ubicacion
            )

    
    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.libreria.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.libreria.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.libreria.mostrar()
        self.ui.salida.insertPlainText(str(self.libreria))