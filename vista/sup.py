from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget, QPushButton

class VistaSUP(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_sup = QTabWidget(self)
        self.layout_sup = QVBoxLayout(self)
        self.layout_sup.addWidget(self.tab_sup)

        self.vista_registrar_contratos_sup = VistaRegistrarContratosSUP()
        self.tab_sup.addTab(self.vista_registrar_contratos_sup, "Registrar contratos")

        self.vista_registrar_cts_sup = VistaRegistrarCTSSUP()
        self.tab_sup.addTab(self.vista_registrar_cts_sup, "Registrar CTS")

    def mostrar_ventana_registrar_contratos_sup(self):
        self.ventana_registrar_contratos_sup = VentanaRegistrarContratosSUP()
        self.ventana_registrar_contratos_sup.show()

    def mostrar_ventana_registrar_cts_sup(self):
        self.ventana_registrar_cts_sup = VentanaRegistrarCTSSUP()
        self.ventana_registrar_cts_sup.show()

class VistaRegistrarContratosSUP(QWidget):
    def __init__(self):
        super().__init__()

        boton_registrar_contratos_sup = QPushButton("Registrar contratos")
        boton_registrar_contratos_sup.clicked.connect(self.mostrar_ventana_registrar_contratos_sup)

        label_registrar_contratos_sup = QLabel("Estás en la subpestaña Registrar contratos de SUP")
        layout_registrar_contratos_sup = QVBoxLayout()
        layout_registrar_contratos_sup.addWidget(label_registrar_contratos_sup)
        layout_registrar_contratos_sup.addWidget(boton_registrar_contratos_sup)
        self.setLayout(layout_registrar_contratos_sup)

    def mostrar_ventana_registrar_contratos_sup(self):
        self.parent().mostrar_ventana_registrar_contratos_sup()

class VistaRegistrarCTSSUP(QWidget):
    def __init__(self):
        super().__init__()

        boton_registrar_cts_sup = QPushButton("Registrar CTS")
        boton_registrar_cts_sup.clicked.connect(self.mostrar_ventana_registrar_cts_sup)

        label_registrar_cts_sup = QLabel("Estás en la subpestaña Registrar CTS de SUP")
        layout_registrar_cts_sup = QVBoxLayout()
        layout_registrar_cts_sup.addWidget(label_registrar_cts_sup)
        layout_registrar_cts_sup.addWidget(boton_registrar_cts_sup)
        self.setLayout(layout_registrar_cts_sup)

    def mostrar_ventana_registrar_cts_sup(self):
        self.parent().mostrar_ventana_registrar_cts_sup()
