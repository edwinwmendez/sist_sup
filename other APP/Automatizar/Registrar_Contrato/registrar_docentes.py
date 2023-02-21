import pandas as pd
import pyautogui
import planilla
from colorama import init, Fore, Style, Back
# Para iniciar colorama
init()

tiempo_inicio = 5
time_pass = 0.3

nombre_columnas = [
    'modular',
    'cod_plaza',
    'rdl',
    'cod_regimen',
    'tipo_afp',
    'cuspp',
    'fecha_afil',
    'fecha_devengue',
    'nivel_magisterial',
    'decima',
    'leyenda',
    'dias_laborados',
    'cuenta']

df = pd.read_csv("bd_contratos_2022.csv", names=nombre_columnas)

filas = len(df.axes[0])
columnas = len(df.axes[1])

print("\nTotal Registros a procesar: ", filas-1, "\n")
#print("Columnas: ", columnas)


def run():
    for i in range(len(df)):
        if i != 0:
            modular = df["modular"][i]
            cod_plaza = df["cod_plaza"][i]
            rdl = df["rdl"][i]
            cod_regimen = df["cod_regimen"][i]
            tipo_afp = df["tipo_afp"][i]
            cuspp = df["cuspp"][i]
            fecha_afil = df["fecha_afil"][i]
            fecha_devengue = df["fecha_devengue"][i]
            nivel_magisterial = df["nivel_magisterial"][i]
            decima = df["decima"][i]
            leyenda = df["leyenda"][i]
            dias_laborados = df["dias_laborados"][i]
            cuenta = df["cuenta"][i]
            #print("Comenzando a registrar a ", modular)
            planilla.buscar_modular(modular)
            planilla.clic_nuevo()
            planilla.ingresar_codigo_plaza(cod_plaza)
            planilla.ingresar_documento_referencia(rdl)
            planilla.ingresar_regimen_pensionario(cod_regimen, tipo_afp, cuspp, fecha_afil, fecha_devengue)
            planilla.ingresar_nivel_magisterial(nivel_magisterial)
            #planilla.ingresar_decima(decima)
            planilla.ingresar_leyenda(leyenda) 
            #planilla.ingresar_dias_laborados(dias_laborados)
            planilla.ingresar_cuenta(cuenta)
            planilla.clic_ingresar()
            planilla.clic_cerrar()
            print(Fore.GREEN +"INFO> \t ", Fore.RESET +"Procesado a ", end=""),
            print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + " " + modular, Fore.RESET + Style.RESET_ALL + "--->", i, "de", filas-1)
    print("\n Procesos terminados correctamente \n")

if __name__ == '__main__':
    run()
