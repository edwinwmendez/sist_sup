from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget, QPushButton

class VistaAyuda(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_ayuda = QTabWidget(self)
        self.layout_ayuda = QVBoxLayout(self)
        self.layout_ayuda.addWidget(self.tab_ayuda)

        self.vista_comunicarse_soporte_tecnico = VistaComunicarseSoporteTecnico()
        self.tab_ayuda.addTab(self.vista_comunicarse_soporte_tecnico, "Comunicarse con Soporte Técnico")

        self.vista_manual = VistaManual()
        self.tab_ayuda.addTab(self.vista_manual, "Manual")
