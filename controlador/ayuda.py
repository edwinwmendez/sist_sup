class ControladorAyuda:
    def __init__(self, vista_ayuda):
        self.vista_ayuda = vista_ayuda

        self.vista_ayuda.vista_comunicarse_soporte_t.boton_comunicarse_soporte_tecnico.clicked.connect(self.mostrar_ventana_comunicarse_soporte_tecnico)

    def mostrar_ventana_comunicarse_soporte_tecnico(self):
        self.vista_ayuda.mostrar_ventana_comunicarse_soporte_tecnico()

