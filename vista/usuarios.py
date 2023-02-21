from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget, QPushButton

class VistaUsuarios(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_usuarios = QTabWidget(self)
        self.layout_usuarios = QVBoxLayout(self)
        self.layout_usuarios.addWidget(self.tab_usuarios)

        self.vista_crear_usuario = VistaCrearUsuario()
        self.tab_usuarios.addTab(self.vista_crear_usuario, "Crear")

        self.vista_administrar_usuarios = VistaAdministrarUsuarios()
        self.tab_usuarios.addTab(self.vista_administrar_usuarios, "Administrar")

    def mostrar_ventana_crear_usuario(self):
        self.ventana_crear_usuario = VentanaCrearUsuario()
        self.ventana_crear_usuario.show()

class VistaCrearUsuario(QWidget):
    def __init__(self):
        super().__init__()

        boton_crear_usuario = QPushButton("Crear usuario")
        boton_crear_usuario.clicked.connect(self.mostrar_ventana_crear_usuario)

        label_crear_usuario = QLabel("Estás en la subpestaña Crear usuario")
        layout_crear_usuario = QVBoxLayout()
        layout_crear_usuario.addWidget(label_crear_usuario)
        layout_crear_usuario.addWidget(boton_crear_usuario)
        self.setLayout(layout_crear_usuario)

    def mostrar_ventana_crear_usuario(self):
        self.parent().mostrar_ventana_crear_usuario()

class VistaAdministrarUsuarios(QWidget):
    def __init__(self):
        super().__init__()

        label_administrar_usuarios = QLabel("Estás en la subpestaña Administrar usuarios")
        layout_administrar_usuarios = QVBoxLayout()
        layout_administrar_usuarios.addWidget(label_administrar_usuarios)
        self.setLayout(layout_administrar_usuarios)
