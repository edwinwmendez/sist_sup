from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget
from vista.sup import VistaSUP
from vista.acm import VistaACM
from vista.mcap import VistaMCAP

class VistaConfiguracion(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_configuracion = QTabWidget(self)
        self.layout_configuracion = QVBoxLayout(self)
        self.layout_configuracion.addWidget(self.tab_configuracion)

        self.vista_sup = VistaSUP()
        self.tab_configuracion.addTab(self.vista_sup, "SUP")

        self.vista_acm = VistaACM()
        self.tab_configuracion.addTab(self.vista_acm, "ACM")

        self.vista_mcap = VistaMCAP()
        self.tab_configuracion.addTab(self.vista_mcap, "MCAP")
