import pyautogui
import pyperclip

tiempo_inicio = 2
time_pass = 0.5
periodo = "202203"


def borrar_campo(cantidad):
    pyautogui.press('delete', presses=cantidad)
    pyautogui.press('backspace', presses=cantidad)


def pausar(tiempo):
    pyautogui.sleep(tiempo)


def mover(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def buscar_modular(modular):
    """Esta función permitirá ingresar el código modular y dar clic en Buscar"""
    pausar(tiempo_inicio)
    mover(750, 140)
    borrar_campo(15)
    pyautogui.write(modular)
    pyautogui.press("tab", presses=1)
    pyautogui.press("space")
    pausar(time_pass)

def seleccionar_registro():
    pausar(time_pass)
    pyautogui.alert("Seleccione y abra el registro del docente")
    pausar(time_pass*2)

def clic_nuevo():
    # Hacemos clic en Nuevo
    mover(500, 445)
    pausar(1.3)


def clic_ingresar():
    # Hacemos clic en Ingresar
    mover(425,720)
    pyautogui.sleep(time_pass)
    pyautogui.press("space")
    pyautogui.sleep(time_pass)
    pyautogui.press("space")
    pyautogui.sleep(time_pass)


def clic_actualizar():
    # Hacemos clic en actualizar
    mover(330, 620)
    pyautogui.sleep(time_pass)
    pyautogui.press("space")
    pyautogui.sleep(time_pass)


def clic_cerrar():
    mover(1130,720)
    pyautogui.sleep(time_pass)


def ingresar_codigo_plaza(cod_plaza):
    mover(820,480)
    borrar_campo(12)
    pyautogui.write(cod_plaza)
    mover(910,480)
    pausar(time_pass)


def ingresar_documento_referencia(rdl):
    mover(460,460)
    borrar_campo(21)
    pyautogui.write(rdl)
    pausar(time_pass)


def ingresar_regimen_pensionario(cod_regimen, tipo_afp, cuspp, fecha_afil, fecha_devengue):
    mover(460,560)
    pyautogui.write(cod_regimen)
    if cod_regimen == "2":
        pausar(time_pass)
    else:
        pyautogui.write(tipo_afp)
        pyautogui.press("tab", presses=2)
        pyautogui.write(cuspp)
        pyautogui.press("tab", presses=1)
        pyautogui.write(fecha_afil)
        pyautogui.press("tab", presses=1)
        pyautogui.write(fecha_devengue)
        pyautogui.press("tab", presses=1)
    pausar(time_pass)


def ingresar_nivel_magisterial(nivel_magisterial):
    mover(715,550)
    borrar_campo(1)
    pyautogui.write(nivel_magisterial)
    pausar(time_pass)


def ingresar_cargo(cargo):
    mover(840, 350)
    borrar_campo(4)
    pyautogui.write(cargo)
    pausar(time_pass)


def ingresar_leyenda(leyenda):
    mover(850,650)
    borrar_campo(50)
    pyautogui.write(leyenda)
    pausar(time_pass)

    
def ingresar_leyenda_mensual():
    mover(400, 547)
    borrar_campo(10)
    pyautogui.write(periodo)
    pausar(time_pass)


def ingresar_decima(decima):
    mover(1010,385)
    borrar_campo(2)
    pyautogui.write(decima)
    pausar(time_pass)
    

def ingresar_dias_laborados(dias_laborados):
    mover(1010,340)
    borrar_campo(2)
    pyautogui.write(dias_laborados)
    pausar(time_pass)


def ingresar_cuenta(cuenta):
    if cuenta == "0":
        print("No tiene cuenta")
        pausar(time_pass)
    else:
        mover(990,670)
        borrar_campo(3)
        pyautogui.write("2")
        pyautogui.press("tab", presses=2)
        pyautogui.write(cuenta)
        pausar(time_pass)


def abrir_habilitado():
    #Seleccionar uno por uno hasta encontrar el que tenga código de situación 55 "Pago Ocasional"
    coord_x_registro = 875
    coord_y_registro = 225
    pyautogui.sleep(1)
    for i in range(1, 50, 1):

        #Clic en el primero
        pyautogui.sleep(time_pass)
        pyautogui.moveTo(coord_x_registro,coord_y_registro)
        pyautogui.doubleClick()
        pyautogui.sleep(time_pass)

        #Seleccionamos lo que contiene el campo situación
        pyautogui.keyDown('shift')
        pyautogui.press('right', presses=2)
        pyautogui.keyUp('shift')
        pyautogui.sleep(time_pass)      
        pyautogui.hotkey('ctrl', 'c', interval = 0.15)

        #Guardamos el contenido del portapapeles en la variable
        situacion = pyperclip.paste()
        
        coord_y_registro = coord_y_registro + 16
        if situacion == "4":
            #Ingresamos Haberes
            #print("Registro habilitado encontrado")
            break
        else:
            #Cerramos la ventana
            #print("No encontramos el registro")
            clic_cerrar()

def cambiar_situacion(situacion):
    pyautogui.write(situacion)
    pausar(time_pass)


def copiar_decima():
    # Nos ubicamos en el campo Decima
    mover(835, 285)
    # Seleccionamos lo que contiene el campo codigo Modular
    pyautogui.keyDown('shift')
    pyautogui.press('right', presses=2)
    pyautogui.keyUp('shift')
    pyautogui.sleep(time_pass)
    pyautogui.hotkey('ctrl', 'c', interval=0.15)

    # Guardamos el contenido del portapapeles en la variable
    decima = pyperclip.paste()
    pausar(time_pass)
    return decima


def abrir_haberes():
    # Hacemos clic en Haberes
    mover(420, 620)
    pausar(3)

def cerrar_haberes():
    # Hacemos clic en cerrar para cerrar la ventana haberes
    mover(637, 445)
    pausar(time_pass)

def agregar_haber(cod_haber,monto):
    pausar(time_pass)
    mover(340, 445)
    pausar(time_pass)
    borrar_campo(1)
    pyautogui.write(cod_haber)
    pyautogui.press("tab", presses=2)
    pyautogui.write(monto)
    pyautogui.press("tab", presses=1)
    borrar_campo(6)
    pyautogui.write(periodo)
    pyautogui.press("tab", presses=1)
    borrar_campo(6)
    pyautogui.write(periodo)
    pyautogui.press("tab", presses=2)
    pyautogui.press("space")
    pausar(time_pass)
    pyautogui.press("space")