from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget

class VistaMCAP(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_mcap = QTabWidget(self)
        self.layout_mcap = QVBoxLayout(self)
        self.layout_mcap.addWidget(self.tab_mcap)

        self.vista_destacar_lrm = VistaDestacarLRM()
        self.tab_mcap.addTab(self.vista_destacar_lrm, "Destacar LRM")

        self.vista_reasignar_lrm = VistaReasignarLRM()
        self.tab_mcap.addTab(self.vista_reasignar_lrm, "Reasignar LRM")

        self.vista_encargatura = VistaEncargatura()
        self.tab_mcap.addTab(self.vista_encargatura, "Encargatura")

        self.vista_ubicar_docente = VistaUbicarDocente()
        self.tab_mcap.addTab(self.vista_ubicar_docente, "Ubicar Docente")

class VistaDestacarLRM(QWidget):
    def __init__(self):
        super().__init__()

        label_destacar_lrm = QLabel("Estás en la subpestaña Destacar LRM")
        layout_destacar_lrm = QVBoxLayout()
        layout_destacar_lrm.addWidget(label_destacar_lrm)
        self.setLayout(layout_destacar_lrm)

class VistaReasignarLRM(QWidget):
    def __init__(self):
        super().__init__()

        label_reasignar_lrm = QLabel("Estás en la subpestaña Reasignar LRM")
        layout_reasignar_lrm = QVBoxLayout()
        layout_reasignar_lrm.addWidget(label_reasignar_lrm)
        self.setLayout(layout_reasignar_lrm)

class VistaEncargatura(QWidget):
    def __init__(self):
        super().__init__()

        label_encargatura = QLabel("Estás en la subpestaña Encargatura")
        layout_encargatura = QVBoxLayout()
        layout_encargatura.addWidget(label_encargatura)
        self.setLayout(layout_encargatura)

class VistaUbicarDocente(QWidget):
    def __init__(self):
        super().__init__()

        label_ubicar_docente = QLabel("Estás en la subpestaña Ubicar Docente")
        layout_ubicar_docente = QVBoxLayout()
        layout_ubicar_docente.addWidget(label_ubicar_docente)
        self.setLayout(layout_ubicar_docente)

