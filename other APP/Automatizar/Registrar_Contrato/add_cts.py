from tkinter.font import names
import pandas as pd
import sys
import pyautogui
import pyperclip

periodo = "202321"
tiempo_abrir_haberes = 3.5
tiempo_pasar_campos = 0.3
tiempo_inicio = 0.5

df = pd.read_csv("bd_cts.csv")
# print(df.iloc[0, 0])

nombre_columnas = ['orden',
                   'modular',
                   'monto']

df = pd.read_csv("bd_cts.csv", names=nombre_columnas)
# print(df.iloc[0, 0])

filas = len(df.axes[0])
columnas = len(df.axes[1])

seleccionar_registro_ocasional = "seleccionar_registro_ocasional.png"
codigo_modular = "codigo_modular.png"
leyenda_mensual = "leyenda_mensual.png"
btn_buscar = "btn_buscar.png"
btn_empleados_nuevo = "btn_empleados_nuevo.png"
btn_pago_ocasional = "btn_pago_ocasional.png"
btn_registro_actualizar = "btn_registro_actualizar.png"
btn_registro_cerrar = "btn_registro_cerrar.png"
btn_registro_haberes = "btn_registro_haberes.png"
btn_registro_ingresar = "btn_registro_ingresar.png"


def clic_imagen(imagen):
    while True:
        location = pyautogui.locateOnScreen(imagen)
        if location:
            x, y = pyautogui.center(location)
            pyautogui.click(x, y)
            break
        else:
            print(f"Imagen {imagen} no encontrada")
            confirm = input(
                "Por favor, posicione la imagen en la pantalla ¿Desea continuar? (s/n): ")
            if confirm.lower() == "s":
                continue
            else:
                print("Invalid input")


def doble_clic_imagen(imagen):
    while True:
        location = pyautogui.locateOnScreen(imagen)
        if location:
            x, y = pyautogui.center(location)
            pyautogui.doubleClick(x, y)
            break
        else:
            print(f"Imagen {imagen} no encontrada")
            confirm = input(
                "Por favor, posicione la imagen en la pantalla ¿Desea continuar? (s/n): ")
            if confirm.lower() == "s":
                continue
            else:
                print("Invalid input")

    # try:
    #     image_position = pyautogui.locateOnScreen(imagen)
    #     x, y = pyautogui.center(image_position)
    #     pyautogui.doubleClick(x, y)
    # except TypeError:
    #     print(f"No se encontró la imagen {imagen} en la pantalla")
    #     print(f"El programa se cerrara")
    #     sys.exit()


def ingresar_y_buscar(modular):
    """Esta función permitirá ingresar el código modular y dar clic en Buscar"""
    pyautogui.sleep(tiempo_inicio)
    clic_imagen(codigo_modular)
    # pyautogui.moveTo(765, 430)
    # pyautogui.click()
    pyautogui.press('delete', presses=15)
    pyautogui.press('backspace', presses=15)
    pyautogui.write(modular)
    pyautogui.press("tab", presses=1)
    pyautogui.press("space")


def crear_registro(modular):
    """ Creará un nuevo registro de pago ocasional, si ya está creado, solo se habilitará y actualizará """
    # Ingresamos el código modular y damos clic en Buscar
    ingresar_y_buscar(modular)
    # Hacemos clic en Pagos Ocacionales
    clic_imagen(btn_pago_ocasional)
    pyautogui.sleep(1.6)
    # Hacemos clic en Ingresar
    clic_imagen(btn_registro_ingresar)
    pyautogui.press("space")
    pyautogui.sleep(tiempo_pasar_campos)
    pyautogui.press("space")
    pyautogui.sleep(tiempo_pasar_campos)
    # Hacemos clic en actualizar
    clic_imagen(btn_registro_actualizar)
    pyautogui.press("space")
    pyautogui.sleep(tiempo_pasar_campos)
    # Cerramos la ventana
    cerrar_ventana_registro_first()


def ingresar_haber(monto):
    """ Esta función sirve para crear un nuevo haber con código de pago CTS"""
    # nosubicamosenelbotonhaberesyhacemosclic
    pyautogui.moveTo(590, 720)
    pyautogui.click()

    pyautogui.sleep(tiempo_abrir_haberes)
    # Agregamosunnuevohaber
    pyautogui.press('space')
    pyautogui.sleep(tiempo_pasar_campos)
    pyautogui.press('delete', presses=3)
    pyautogui.press('backspace', presses=3)
    pyautogui.write("276")
    pyautogui.press('tab', presses=2)
    # Escribimos el monto
    pyautogui.write(monto)
    pyautogui.press('tab')
    # Borramos el contenido del periodo
    pyautogui.press('delete', presses=10)
    pyautogui.press('backspace', presses=10)
    pyautogui.write(periodo)
    pyautogui.press('tab')
    # Borramos el contenido del periodo
    pyautogui.press('delete', presses=10)
    pyautogui.press('backspace', presses=10)
    pyautogui.write(periodo)
    # Nos ubbicamos en el botón Ingresar
    pyautogui.press('tab', presses=2)
    # Presionamos el botón Ingresar
    pyautogui.press('space')
    pyautogui.sleep(0.3)
    # Nos ubicamos en el botón Cerrar y lo presionamos
    pyautogui.press('space')
    pyautogui.sleep(0.3)
    # cerrar la ventana de haberes
    pyautogui.press('tab', presses=2)
    pyautogui.press('space')
    pyautogui.sleep(0.3)
    # Agregamos la leyenda mensual
    ingresamos_leyenda_mensual()
    # Actualizamos el registro
    actualizar_registro()


def ingresamos_leyenda_mensual():
    # Nosubicamosenelcampo de leyenda mensual
    clic_imagen(leyenda_mensual)
    pyautogui.press('delete', presses=15)
    pyautogui.press('backspace', presses=15)
    pyautogui.write(periodo)
    pyautogui.sleep(tiempo_pasar_campos)


def cerrar_ventana_registro_first():
    clic_imagen(btn_registro_cerrar)
    pyautogui.sleep(0.7)


def cerrar_ventana_registro():
    clic_imagen(btn_registro_cerrar)
    pyautogui.sleep(0.9)
    pyautogui.press('tab', presses=17)
    pyautogui.press('delete', presses=15)
    pyautogui.press('backspace', presses=15)
    pyautogui.click(30, 30)


def ingresar_al_registro(posicion, modular):
    """ Esta función sirve para ingresar al registro del docente seleccionado"""
    # Ingresamos el código modular y damos clic en Buscar
    # ingresar_y_buscar(modular)
    pyautogui.sleep(0.6)

    doble_clic_imagen(seleccionar_registro_ocasional)
    print(posicion, ": Ingresando CTS para: ", modular)
    ingresar_haber(monto)
    cerrar_ventana_registro()
    # print("Registrado con éxito")
    import datetime
    import datetime

    def log_event(event,):
        timestamp = str(datetime.datetime.now())
        log_line = timestamp + " - " + event + "\n"
        with open("event_log.txt", "a") as log_file:
            log_file.write(log_line)

            # Registramos a continuacion el texto q se guardara en el archivo log
    log_event(f"{posicion}: {modular} ...ok.")


def actualizar_registro():
    """ Esta función sirve para actualizar el registro luego de haber realizado cualquier modificación a la misma"""
    # Nos ubicamos en el botón Actualizar
    pyautogui.moveTo(500, 720)
    pyautogui.click()
    pyautogui.sleep(tiempo_pasar_campos)
    pyautogui.press("space")


df_original = df.copy()
rows_to_drop = []

pyautogui.sleep(1.5)
try:
    for i, row in df.iterrows():
        if i != 0:
            orden = df["orden"][i]
            monto = str(df["monto"][i])
            modular = df["modular"][i]

            # print(monto, " ", type(monto), modular,)
            crear_registro(modular)
            ingresar_al_registro(orden, modular)
            rows_to_drop.append(i)
            # Eliminamos la fila actual
    df = df.drop(rows_to_drop)
    df.to_csv("data.csv", index=False)

except Exception as e:
    print(e)
