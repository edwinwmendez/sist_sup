from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QGridLayout, QHBoxLayout, QVBoxLayout,
                             QFileDialog, QMessageBox)


class VentanaRegistroContratos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modulo de Registro de Contratos")
        self.initUI()

    def initUI(self):
        # Crear widgets
        lbl_encabezado = QLabel("Modulo de Registro de Contratos")
        lbl_indicaciones = QLabel("Antes de iniciar el proceso de registro de contratos, "
                                  "asegurese de tener el archivo csv registrado tal y como se detalla en el manual.")

        self.lbl_archivo = QLabel("Archivo CSV: ")
        self.le_ruta_archivo = QLineEdit()
        self.btn_examinar = QPushButton("Examinar")
        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_ejecutar.setEnabled(False)

        # Crear layouts
        layout_grid = QGridLayout()
        layout_grid.addWidget(lbl_encabezado, 0, 0)
        layout_grid.addWidget(lbl_indicaciones, 1, 0)
        layout_grid.addWidget(self.lbl_archivo, 2, 0)
        layout_grid.addWidget(self.le_ruta_archivo, 2, 1)
        layout_grid.addWidget(self.btn_examinar, 2, 2)
        layout_h = QHBoxLayout()
        layout_h.addStretch(1)
        layout_h.addWidget(self.btn_ejecutar)
        layout_v = QVBoxLayout()
        layout_v.addLayout(layout_grid)
        layout_v.addLayout(layout_h)

        # Establecer layout principal
        self.setLayout(layout_v)

        # Conectar señales y slots
        self.btn_examinar.clicked.connect(self.seleccionar_archivo)
        self.btn_ejecutar.clicked.connect(self.registrar_contratos)



    def seleccionar_archivo(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos CSV (*.csv)")
        if ruta_archivo:
            self.le_ruta_archivo.setText(ruta_archivo)
            self.btn_ejecutar.setEnabled(True)

    def registrar_contratos(self):
        # Agregar código para el registro de contratos
        pass


class VentanaRegistroCTS(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modulo de Registro de CTS")
        self.initUI()

    def initUI(self):
        # Crear widgets
        lbl_encabezado = QLabel("Modulo de Registro de CTS")
        lbl_indicaciones = QLabel("Antes de iniciar el proceso de registro de CTS, "
                                  "asegurese de tener el archivo csv registrado tal y como se detalla en el manual.")

        self.lbl_archivo = QLabel("Archivo CSV: ")
        self.le_ruta_archivo = QLineEdit()
        self.btn_examinar = QPushButton("Examinar")
        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_ejecutar.setEnabled(False)

        # Crear layout
        layout = QVBoxLayout()
        layout.addWidget(lbl_encabezado)
        layout.addWidget(lbl_indicaciones)
        layout.addStretch(1)
        layout.addWidget(self.lbl_archivo)
        layout.addWidget(self.le_ruta_archivo)
        layout.addWidget(self.btn_examinar)
        layout.addWidget(self.btn_ejecutar)

        # Conectar señales
        self.btn_examinar.clicked.connect(self.abrir_dialogo)
        self.btn_ejecutar.clicked.connect(self.registrar_cts)

        # Establecer layout en la ventana
        self.setLayout(layout)

    def abrir_dialogo(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", "",
                                                 "CSV Files (*.csv)", options=opciones)
        if archivo:
            self.le_ruta_archivo.setText(archivo)
            self.btn_ejecutar.setEnabled(True)

    def registrar_cts(self):
        ruta_archivo = self.le_ruta_archivo.text()
        # TODO: Implementar lógica para registrar CTS desde archivo CSV
        QMessageBox.information(self, "Registro de CTS", "El registro de CTS ha sido completado con éxito.")

