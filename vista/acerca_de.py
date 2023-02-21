from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget, QPushButton

class VistaAcercaDe(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_acerca_de = QTabWidget(self)
        self.layout_acerca_de = QVBoxLayout(self)
        self.layout_acerca_de.addWidget(self.tab_acerca_de)

        self.vista_buscar_actualizaciones = VistaBuscarActualizaciones()
        self.tab_acerca_de.addTab(self.vista_buscar_actualizaciones, "Buscar Actualizaciones")

        self.vista_version = VistaVersion()
        self.tab_acerca_de.addTab(self.vista_version, "Versión")
