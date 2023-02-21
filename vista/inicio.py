from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class VistaInicio(QWidget):
    def __init__(self):
        super().__init__()

        label_inicio = QLabel("Estás en la pestaña Inicio")
        layout_inicio = QVBoxLayout()
        layout_inicio.addWidget(label_inicio)
        self.setLayout(layout_inicio)
