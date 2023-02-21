from shutil import move
import pyautogui
import pyperclip

tiempo_inicio = 3
time_pass = 0.2


def borrar_campo(cantidad):
    pyautogui.press('delete', presses=cantidad)
    pyautogui.press('backspace', presses=cantidad)


def pausar(tiempo):
    pyautogui.sleep(tiempo)


def mover(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def buscar_nombre(clave8_ant):
    pausar(tiempo_inicio)
    mover(200, 200)
    borrar_campo(10)
    pyautogui.write(clave8_ant)
    pyautogui.press("tab", presses=1)
    pyautogui.press("space")
    pausar(time_pass)


def clic_aceptar():
    mover(270, 425)
    pausar(1)


def clic_modificar():
    mover(215, 170)
    pausar(1)


def check_habilitar():
    mover(673, 278)
    pausar(time_pass)


def check_rural():
    mover(673, 253)
    pausar(time_pass)


def copiar_modular_ce():
    # Nos ubicamos en el campo codigo modular
    mover(640, 580)
    # Seleccionamos lo que contiene el campo codigo Modular
    pyautogui.keyDown('shift')
    pyautogui.press('right', presses=10)
    pyautogui.keyUp('shift')
    pyautogui.sleep(time_pass)
    pyautogui.hotkey('ctrl', 'x', interval=0.15)
    
    # Guardamos el contenido del portapapeles en la variable
    modular_ce = pyperclip.paste()
    return modular_ce


def copiar_modular_local():
    # Nos ubicamos en el campo modular_local
    mover(295, 580)
    # Seleccionamos lo que contiene el modular local
    pyautogui.keyDown('shift')
    pyautogui.press('right', presses=10)
    pyautogui.keyUp('shift')
    pyautogui.sleep(time_pass)
    pyautogui.hotkey('ctrl', 'x', interval=0.15)

    # Guardamos el contenido del portapapeles en la variable
    modular_local = pyperclip.paste()
    return modular_local


def clic_actualizar():
    # Hacemos clic en actualizar
    mover(285, 650)
    pyautogui.press("space")
    pyautogui.sleep(1)


def clic_nuevo():
    # Hacemos clic en Nuevo
    mover(200, 430)
    pausar(1.3)


def clic_ingresar():
    # Hacemos clic en Ingresar
    mover(215, 650)
    pausar(time_pass)
    pyautogui.press("space")
    pyautogui.sleep(time_pass)


def ingresar_unid_ejecutora(unid_ejecutora):
    mover(315, 270)
    borrar_campo(2)
    pyautogui.write(unid_ejecutora)
    pausar(time_pass)


def ingresar_nec(nec):
    mover(315, 290)
    borrar_campo(2)
    pyautogui.write(nec)
    pausar(time_pass)


def ingresar_nivel(nivel):
    mover(315, 315)
    borrar_campo(2)
    pyautogui.write(nivel)
    pausar(time_pass)


def ingresar_cod_establecimiento(cod_establecimiento):
    mover(315, 335)
    borrar_campo(2)
    pyautogui.write(cod_establecimiento)
    pausar(time_pass)


def ingresar_departamento(departamento):
    mover(315, 380)
    borrar_campo(2)
    pyautogui.write(departamento)
    pausar(time_pass)


def ingresar_provincia(provincia):
    mover(315, 400)
    borrar_campo(2)
    pyautogui.write(provincia)
    pausar(time_pass)


def ingresar_distrito(distrito):
    mover(315, 425)
    borrar_campo(2)
    pyautogui.write(distrito)
    pausar(time_pass)


def ingresar_centro_costo(centro_costo):
    mover(315, 490)
    borrar_campo(2)
    pyautogui.write(centro_costo)
    pausar(time_pass)


def ingresar_lugar_pago():
    mover(510, 513)
    pausar(time_pass)
    mover(450, 530)
    pausar(time_pass)


def clic_cerrar():
    mover(835, 650)
    pausar(1)


def clic_salir():
    mover(890, 170)
    pausar(time_pass)
