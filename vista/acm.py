from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget, QPushButton

class VistaACM(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_acm = QTabWidget(self)
        self.layout_acm = QVBoxLayout(self)
        self.layout_acm.addWidget(self.tab_acm)

        self.vista_modificar_datos = VistaModificarDatos()
        self.tab_acm.addTab(self.vista_modificar_datos, "Modificar Datos")

        self.vista_registrar_nuevo_trabajador = VistaRegistrarNuevoTrabajador()
        self.tab_acm.addTab(self.vista_registrar_nuevo_trabajador, "Registrar Nuevo Trabajador")

        self.vista_actualizar_datos_trabajador = VistaActualizarDatosTrabajador()
        self.tab_acm.addTab(self.vista_actualizar_datos_trabajador, "Actualizar Datos Trabajador")
