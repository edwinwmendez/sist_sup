from PyQt5.QtCore import Qt
import pyautogui
from position_cursor_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        # Definimos variables globales
        resolucion_pantalla = pyautogui.size()
        ancho_pantalla = resolucion_pantalla[0]
        alto_pantalla = resolucion_pantalla[1]
        ancho_programa = 500
        alto_programa = 70
        posicion_x_programa = ancho_pantalla/2-ancho_programa/2
        posicion_y_programa = alto_pantalla-60-alto_programa

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # Hacer que la ventana siempre se mantenga por encima de todas las demás
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # Ocultamos la barra de titulo
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Asignamos la posición que en pantalla del programa, así como su andho y alto
        self.setGeometry(posicion_x_programa, posicion_y_programa,
                         ancho_programa, alto_programa)
        # Cuando hacemos clic en el círculo rojo, se cierra la ventana, también funciona  presionando la tecla ESC
        self.btn_close.clicked.connect(exit)
        # Cuando hacemos clic en el btn_ok, se ejecutará la función Obtener_Coordenadas()
        self.btn_ok.clicked.connect(self.Obtener_Coordenadas)

    def Obtener_Coordenadas(self):
        # Tomamos el valor del spin(donde seleccionar los numeritos) spn_seconds para usarlo luego
        seconds = int(self.spn_seconds.text())
        # Esperamos {seconds} segundos para obtener la posición del cursor
        pyautogui.sleep(seconds)
        # Obtener las coordenadas X,Y de la posición del Cursor
        coordenada = pyautogui.position()
        # Guardamos la coordenada x, en la variable valor_x
        valor_x = coordenada[0]
        # Guardamos la coordenada y, en la variable valor_y
        valor_y = coordenada[1]
        self.lbl_coord_x.setText(str(valor_x))
        self.lbl_coord_y.setText(str(valor_y))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
