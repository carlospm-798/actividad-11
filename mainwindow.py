"""
Carlos Paredes Márquez.
Importar window a code. xd
28/10/2020.
"""
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from random import randint
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

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_particula)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.id_ascendente_pushButton.clicked.connect(self.id_ascendente)
        self.ui.distancia_descendente_pushButton.clicked.connect(self.distancia_descendente)
        self.ui.velocidad_ascendente_pushButton.clicked.connect(self.velocidad_ascendente)
    
    @Slot()
    def id_ascendente(self):
        print('id ascendente')
        
    @Slot()
    def distancia_descendente(self):
        print('distancia descendente')
    
    @Slot()
    def velocidad_ascendente(self):
        print('velocidad ascendente')

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.libreria: #'MainWindow' object has no attribute 'particulas'
            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x, particula.origen_y, 4, 4, pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y, 4, 4, pen)
            self.scene.addLine(particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y, pen)
        
        """for i in range(100):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            color = QColor(r, g, b)
            pen.setColor(color)

            gen_x = randint(0, 500)
            gen_y = randint(0, 500)
            no_x = randint(0, 500)
            no_y = randint(0, 500)

            self.scene.addEllipse(gen_x, gen_y, 3, 3, pen)
            self.scene.addEllipse(no_x, no_y, 3, 3, pen)
            self.scene.addLine(gen_x + 3, gen_y + 3, no_x, no_y, pen)"""
    
    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def buscar_particula(self):
        numero = self.ui.buscar_lineEdit.text()

        encontrado = False

        for particula in self.libreria:
            if int(numero) == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
    
                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)
                
                encontrado = True
                
                return

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula con la id "{id}" no fue encontrada'
            )
    
    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ['ID', 'origen x', 'origen y', 'destino x', 'destino y', 'velocidad', 'red', 'green', 'blue', 'distancia']
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.libreria))

        row = 0

        for particula in self.libreria:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1
    
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