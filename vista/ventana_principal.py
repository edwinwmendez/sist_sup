from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QLabel, QVBoxLayout, QWidget, QToolButton, QPushButton, \
    QFormLayout, QFrame, QFileDialog, QHBoxLayout, QLineEdit, QDesktopWidget, QMessageBox

from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QFrame

from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtCore import Qt, QSize


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Crear acciones
        self.actionSalir = QAction('&Salir', self)
        self.actionSalir.setShortcut('Ctrl+Q')
        self.actionSalir.triggered.connect(qApp.quit)

        self.actionPrincipal = QAction('&Principal', self)
        self.actionPrincipal.setShortcut('Ctrl+P')

        self.actionRegistrar_contratos = QAction('&Registrar contratos', self)
        self.actionRegistrar_contratos.setShortcut('Ctrl+R')
        self.actionRegistrar_contratos.triggered.connect(self.abrir_ventana_registro_contratos)

        self.actionRegistrar_CTS = QAction('&Registrar CTS', self)
        self.actionRegistrar_CTS.setShortcut('Ctrl+T')
        self.actionRegistrar_CTS.triggered.connect(self.abrir_ventana_registro_cts)

        self.actionProcesos = QAction('&Procesos', self)
        self.actionProcesos.setShortcut('Ctrl+S')

        self.actionCrear_usuario = QAction('&Crear usuario', self)
        self.actionCrear_usuario.setShortcut('Ctrl+N')

        self.actionAdministrar_usuarios = QAction('&Administrar usuarios', self)
        self.actionAdministrar_usuarios.setShortcut('Ctrl+A')

        self.actionModificar_Datos = QAction('&Modificar datos', self)
        self.actionModificar_Datos.setShortcut('Ctrl+M')

        # Crear menu principal
        menu_inicio = self.menuBar().addMenu("&Inicio")
        menu_inicio.addAction(self.actionPrincipal)
        menu_inicio.addSeparator()
        menu_inicio.addAction(self.actionSalir)

        menu_acciones = self.menuBar().addMenu("&Acciones")
        menu_acciones.addAction(self.actionRegistrar_contratos)
        menu_acciones.addAction(self.actionRegistrar_CTS)
        menu_acciones.addAction(self.actionProcesos)

        menu_usuarios = self.menuBar().addMenu("&Usuarios")
        menu_usuarios.addAction(self.actionCrear_usuario)
        menu_usuarios.addAction(self.actionAdministrar_usuarios)

        menu_configuracion = self.menuBar().addMenu("&Configuración")
        submenu_sup = menu_configuracion.addMenu("SUP")
        submenu_sup.addAction(self.actionRegistrar_contratos)
        submenu_sup.addAction(self.actionRegistrar_CTS)
        submenu_sup.addAction(self.actionProcesos)
        submenu_acm = menu_configuracion.addMenu("ACM")
        submenu_acm.addAction(self.actionModificar_Datos)

        self.setFixedSize(1000, 600)

    def abrir_ventana_registro_contratos(self):
        self.hide()
        self.ventana_registro_contratos = VentanaRegistroContratos(self)
        self.ventana_registro_contratos.show()

    def abrir_ventana_registro_cts(self):
        self.hide()
        self.ventana_registro_cts = VentanaRegistroCTS(self)
        self.ventana_registro_cts.show()


class VentanaRegistroContratos(QWidget):
    def __init__(self, ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal
        self.setWindowTitle("Módulo de Registro de Contratos")
        self.initUI()

    def initUI(self):
        # Crear widgets
        lbl_encabezado = QLabel("Módulo de Registro de Contratos")
        lbl_encabezado.setFont(QFont('Arial', 10, weight=QFont.Bold))
        lbl_archivo = QLabel("Seleccione el archivo CSV:")
        self.txt_archivo = QLineEdit()
        self.txt_archivo.setReadOnly(True)
        self.btn_examinar = QPushButton("Examinar")
        self.btn_examinar.clicked.connect(self.abrir_dialogo)
        self.lbl_advertencia = QLabel("Advertencia!! \nAntes de iniciar el proceso de registro de contratos, asegúrese de tener el archivo CSV registrado tal y como se detalla en el manual de usuario.")
        self.lbl_advertencia.setStyleSheet("color: gray")
        self.lbl_advertencia.setAlignment(Qt.AlignJustify)
        self.lbl_advertencia.setWordWrap(True)
        self.lbl_advertencia.setFixedHeight(70)
        self.btn_procesar = QPushButton("Procesar")
        self.btn_procesar.setEnabled(False)
        self.btn_procesar.clicked.connect(self.procesar_csv)
        self.btn_procesar.setMaximumWidth(500)

        # Configurar ventana
        self.setWindowTitle("Módulo de Registro de Contratos")
        self.setFixedSize(300, 350)

        # Obtener las dimensiones de la pantalla
        desktop = QDesktopWidget().availableGeometry()
        x = int((desktop.width() - self.width()) / 2)
        y = int(desktop.height() - self.height() - 40)
        self.move(x, y)

        # Configurar layout
        layout = QVBoxLayout()
        layout.addWidget(lbl_encabezado)
        layout.addSpacing(10)
        layout.addWidget(lbl_archivo)
        layout.addWidget(self.txt_archivo)
        layout.addWidget(self.btn_examinar)

        # Layout para el botón procesar
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addWidget(self.btn_procesar)
        h_layout.addStretch(1)
        layout.addSpacing(20)
        layout.addLayout(h_layout)
        layout.addSpacing(20)

        # Línea horizontal
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)
        layout.addSpacing(10)

        # Advertencia
        layout.addWidget(self.lbl_advertencia)

        self.setLayout(layout)

    def closeEvent(self, event):
        self.hide()
        self.ventana_principal.show()

    def abrir_dialogo(self):
        opciones = QFileDialog.Options()
        self.btn_procesar.setEnabled(True)
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "CSV (*.csv)", options=opciones)
        if nombre_archivo:
            self.txt_archivo.setText(nombre_archivo)

    def procesar_csv(self):
        nombre_archivo = self.txt_archivo.text()
        if nombre_archivo:
            # Agregar lógica para procesar el archivo CSV
            print("Procesando archivo CSV:", self.txt_archivo.text())
        else:
            # Mostrar mensaje de error si no se ha seleccionado un archivo
            mensaje_error = QMessageBox()
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.setText("Error: No se ha seleccionado un archivo.")
            mensaje_error.setWindowTitle("Error")
            mensaje_error.exec_()


class VentanaRegistroCTS(QWidget):
    def __init__(self, ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal
        self.setWindowTitle("Módulo de Registro de CTS")
        self.initUI()

    def initUI(self):
        # Crear widgets
        lbl_encabezado = QLabel("Módulo de Registro de CTS")
        lbl_encabezado.setFont(QFont('Arial', 10, weight=QFont.Bold))
        lbl_archivo_csv = QLabel("Seleccione el archivo CSV:")
        self.txt_archivo_csv = QLineEdit()
        self.txt_archivo_csv.setReadOnly(True)
        self.btn_examinar_csv = QPushButton("Examinar")
        self.btn_examinar_csv.clicked.connect(self.abrir_dialogo)
        self.lbl_advertencia = QLabel("Advertencia!! \nAntes de iniciar el proceso de registro de CTS, asegúrese de tener el archivo CSV registrado tal y como se detalla en el manual de usuario.")
        self.lbl_advertencia.setStyleSheet("color: gray")
        self.lbl_advertencia.setAlignment(Qt.AlignJustify)
        self.lbl_advertencia.setWordWrap(True)
        self.lbl_advertencia.setFixedHeight(70)
        self.btn_procesar = QPushButton("Procesar")
        self.btn_procesar.setEnabled(False)
        self.btn_procesar.clicked.connect(self.procesar_csv)
        self.btn_procesar.setMaximumWidth(500)

        # Configurar ventana
        self.setWindowTitle("Módulo de Registro de CTS")
        self.setFixedSize(300, 350)

        # Obtener las dimensiones de la pantalla
        desktop = QDesktopWidget().availableGeometry()
        x = int((desktop.width() - self.width()) / 2)
        y = int(desktop.height() - self.height() - 40)
        self.move(x, y)

        # Configurar layout
        layout = QVBoxLayout()
        layout.addWidget(lbl_encabezado)
        layout.addSpacing(10)
        layout.addWidget(lbl_archivo_csv)
        layout.addWidget(self.txt_archivo_csv)
        layout.addWidget(self.btn_examinar_csv)

        # Layout para el botón procesar
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addWidget(self.btn_procesar)
        h_layout.addStretch(1)
        layout.addSpacing(20)
        layout.addLayout(h_layout)
        layout.addSpacing(20)

        # Línea horizontal
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)
        layout.addSpacing(10)

        # Advertencia
        layout.addWidget(self.lbl_advertencia)

        self.setLayout(layout)

    def closeEvent(self, event):
        self.hide()
        self.ventana_principal.show()

    def abrir_dialogo(self):
        opciones = QFileDialog.Options()
        self.btn_procesar.setEnabled(True)
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "CSV (*.csv)", options=opciones)
        if nombre_archivo:
            self.txt_archivo_csv.setText(nombre_archivo)

    def procesar_csv(self):
        from controlador.registrar_cts import ControladorRegistroCTS as RegistrarCTS

        nombre_archivo = self.txt_archivo_csv.text()
        if nombre_archivo:
            # Crear instancia del controlador RegistrarContratos y llamar al método para procesar el archivo CSV
            controlador = RegistrarCTS()
            controlador.procesar_csv(nombre_archivo)
        else:
            # Mostrar mensaje de error si no se ha seleccionado un archivo
            mensaje_error = QMessageBox()
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.setText("Error: No se ha seleccionado un archivo.")
            mensaje_error.setWindowTitle("Error")
            mensaje_error.exec_()

# Aquí puedes agregar la lógica para procesar el archivo CSV
pass
