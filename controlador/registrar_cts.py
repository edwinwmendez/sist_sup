import pyautogui
from PyQt5.QtWidgets import QMessageBox

from modelo.registrar_cts import CsvProcessor
from vista.ventana_principal import VentanaRegistroCTS


class ControladorRegistroCTS:
    def __init__(self):
        self.ventana_cts = VentanaRegistroCTS(self)


    def procesar_csv(self, nombre_archivo):
        # def crear_registro(modular):
        #     """ Creará un nuevo registro de pago ocasional, si ya está creado, solo se habilitará y actualizará """
        #     try:
        #         # Ingresamos el código modular y damos clic en Buscar
        #         ingresar_y_buscar(modular)
        #         # Hacemos clic en Pagos Ocacionales
        #         clic_imagen(btn_pago_ocasional)
        #         pyautogui.sleep(1.6)
        #         # Hacemos clic en Ingresar
        #         clic_imagen(btn_registro_ingresar)
        #         pyautogui.press("space")
        #         pyautogui.sleep(tiempo_pasar_campos)
        #         pyautogui.press("space")
        #         pyautogui.sleep(tiempo_pasar_campos)
        #         # Hacemos clic en actualizar
        #         clic_imagen(btn_registro_actualizar)
        #         pyautogui.press("space")
        #         pyautogui.sleep(tiempo_pasar_campos)
        #         # Cerramos la ventana
        #         cerrar_ventana_registro_first()
        #         log_event(f"{modular} - Registro creado con éxito")
        #     except ImageNotFoundException:
        #         log_event(f"{modular} - Error: no se encontró alguna imagen")
        #         raise
        #     except:
        #         log_event(f"{modular} - Error: ocurrió un error al crear el registro")
        #         raise


        # Crear instancia de la clase CsvProcessor y llamar al método para leer el archivo
        modelo_csv = CsvProcessor()
        try:
            modelo_csv.read_csv(nombre_archivo)
        except FileNotFoundError:
            QMessageBox.warning(self.ventana_cts, "Error",
                                "El archivo no se encontró. Por favor, seleccione un archivo válido.")
            return
        except Exception as e:
            QMessageBox.critical(self.ventana_cts, "Error", f"Ha ocurrido un error al leer el archivo: {str(e)}")
            return

        # Obtener los datos del DataFrame y recorrerlos fila por fila
        datos = modelo_csv.df.values
        rows_to_drop = []
        for fila in datos:
            # Procesar los datos de la fila como sea necesario
            orden = fila[0]
            modular = fila[1]
            monto = fila[2]
            # Hacer algo con los datos de la fila
            print(f"Orden: {orden}, Modular: {modular}, Monto: {monto}")

            try:
                # crear_registro(modular)
                # ingresar_al_registro(orden, modular, monto)
                rows_to_drop.append(fila)
            except Exception as e:
                QMessageBox.critical(self.ventana_cts, "Error",
                                     f"Ha ocurrido un error al procesar la fila {orden}: {str(e)}")
                return



    def mostrar_ventana_principal(self):
        self.ventana_cts.hide()
