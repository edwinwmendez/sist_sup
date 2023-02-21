import pandas as pd
import pyautogui
import region

tiempo_inicio = 5
time_pass = 0.3

nombre_columnas = [
    'clave8_ant',
    'clave8_new',
    'nombre',
    'unid_ejecutora',
    'nec',
    'nivel',
    'cod_establecimiento',
    'departamento',
    'provincia',
    'distrito',
    'centro_costo']

df = pd.read_csv("bd_migrar_iiee.csv", names=nombre_columnas)

filas = len(df.axes[0])
columnas = len(df.axes[1])

print("Registrando: ", filas-1)
#print("Columnas: ", columnas)


def run():
    region.pausar(5)
    for i in range(len(df)):
        if i != 0:
            clave8_ant = df["clave8_ant"][i]
            clave8_new = df["clave8_new"][i]
            nombre = df["nombre"][i]
            unid_ejecutora = df["unid_ejecutora"][i]
            nec = df["nec"][i]
            nivel = df["nivel"][i]
            cod_establecimiento = df["cod_establecimiento"][i]
            departamento = df["departamento"][i]
            provincia = df["provincia"][i]
            distrito = df["distrito"][i]
            centro_costo = df["centro_costo"][i]

            print("Comenzando a registrar a ", clave8_ant)
            region.buscar_nombre(clave8_ant)
            region.clic_aceptar()
            region.clic_modificar()
            region.check_habilitar()
            modular_ce = region.copiar_modular_ce()
            modular_local = region.copiar_modular_local()
            
            region.clic_actualizar()
            region.clic_cerrar()
            region.clic_salir()
            region.clic_nuevo()
            pyautogui.write(nombre)
            region.check_rural()
            region.check_habilitar()
            region.ingresar_unid_ejecutora(unid_ejecutora)
            region.ingresar_nec(nec)
            region.ingresar_nivel(nivel)

            region.ingresar_cod_establecimiento(cod_establecimiento)
            region.ingresar_departamento(departamento)
            region.ingresar_provincia(provincia)
            region.ingresar_distrito(distrito)
            region.ingresar_centro_costo(centro_costo)
            region.ingresar_lugar_pago()


            print(modular_ce)
            print(modular_local)
            
            region.pausar(1)
            
            # Nos ubicamos en el campo codigo modular CE
            region.mover(650, 580)
            pyautogui.write(modular_ce)
            region.pausar(time_pass)
            
            if modular_ce != modular_local:
                # Nos ubicamos en el campo codigo modular local
                region.mover(332, 580)
                pyautogui.write(modular_local)
                region.pausar(time_pass)
            else:
                print("No se está agregando Modular del local xq no tenia en la iie anterior")

            region.clic_ingresar()
            region.clic_cerrar()

            print("Terminamos de registrar a ", clave8_new)
            print("Se registraron ", i, " registros \n\n")


if __name__ == '__main__':
    run()
