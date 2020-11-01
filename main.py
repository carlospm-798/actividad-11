"""
Carlos Paredes Márquez.
Función principal.
28/10/2020.
"""
from PySide2.QtWidgets import QPushButton, QApplication
from mainwindow import MainWindow
import sys

#App Qt
app = QApplication()
#Ventana
window = MainWindow()
#Función mostrar
window.show()
#Qt loop
sys.exit(app.exec_())
