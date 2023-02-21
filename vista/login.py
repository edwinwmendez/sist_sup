from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.setFixedSize(400, 450)
        self.setWindowModality(Qt.ApplicationModal)

        self.setWindowTitle("Inicio de Sesión")
        self.setStyleSheet("background-color: #0F1618;")

        self.initUI()

    def initUI(self):
        # Logo
        lbl_logo = QLabel()
        pixmap = QPixmap("../recursos/imagenes/logo.png")
        lbl_logo.setPixmap(pixmap)
        lbl_logo.setAlignment(Qt.AlignCenter)

        # Campos de texto
        lbl_usuario = QLabel("Usuario:")
        lbl_usuario.setStyleSheet("color: white")
        self.txt_usuario = QLineEdit()
        self.txt_usuario.setStyleSheet("background-color: #EDEDED")
        lbl_contrasena = QLabel("Contraseña:")
        lbl_contrasena.setStyleSheet("color: white")
        self.txt_contrasena = QLineEdit()
        self.txt_contrasena.setEchoMode(QLineEdit.Password)
        self.txt_contrasena.setStyleSheet("background-color: #EDEDED")

        # Botón de inicio de sesión
        self.btn_ingresar = QPushButton("Ingresar")
        self.btn_ingresar.setStyleSheet("background-color: #DC191B; color: white;")
        self.btn_ingresar.clicked.connect(self.iniciar_sesion)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(lbl_logo)
        layout.addStretch(1)
        form_layout = QVBoxLayout()
        form_layout.addWidget(lbl_usuario)
        form_layout.addWidget(self.txt_usuario)
        form_layout.addWidget(lbl_contrasena)
        form_layout.addWidget(self.txt_contrasena)
        layout.addLayout(form_layout)
        layout.addStretch(1)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch(1)
        btn_layout.addWidget(self.btn_ingresar)
        btn_layout.addStretch(1)
        layout.addLayout(btn_layout)
        layout.addStretch(1)
        self.setLayout(layout)

    def iniciar_sesion(self):
        usuario = self.txt_usuario.text()
        contrasena = self.txt_contrasena.text()
        # TODO: Agregar lógica para iniciar sesión

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaLogin()
    ventana.show()
    app.exec_()
