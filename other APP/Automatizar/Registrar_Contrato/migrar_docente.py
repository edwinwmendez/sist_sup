import pandas as pd
import pyautogui
import planilla

tiempo_inicio = 5
time_pass = 0.3

nombre_columnas = [
    'modular',
    'cod_plaza',
    'rdl',
    'cod_regimen',
    'cuspp',
    'fecha_afil',
    'fecha_devengue',
    'nivel_magisterial',
    'cargo',
    'leyenda',
    'dias_laborados',
    'cuenta']

df = pd.read_csv("bd_contratos_2022.csv", names=nombre_columnas)

filas = len(df.axes[0])
columnas = len(df.axes[1])

print("Filas: ", filas)
print("Columnas: ", columnas)


def run():
    for i in range(len(df)):
        if i != 0:
            modular = df["modular"][i]
            cod_plaza = df["cod_plaza"][i]
            rdl = df["rdl"][i]
            cod_regimen = df["cod_regimen"][i]
            cuspp = df["cuspp"][i]
            fecha_afil = df["fecha_afil"][i]
            fecha_devengue = df["fecha_devengue"][i]
            nivel_magisterial = df["nivel_magisterial"][i]
            cargo = df["cargo"][i]
            leyenda = df["leyenda"][i]
            dias_laborados = df["dias_laborados"][i]
            cuenta = df["cuenta"][i]
            print("Comenzando a registrar a ", modular)
            planilla.buscar_modular(modular)
            planilla.clic_nuevo()
            planilla.ingresar_codigo_plaza(cod_plaza)
            planilla.ingresar_documento_referencia(rdl)
            planilla.ingresar_regimen_pensionario(
                cod_regimen, cuspp, fecha_afil, fecha_devengue)
            planilla.ingresar_nivel_magisterial(nivel_magisterial)
            planilla.ingresar_cargo(cargo)
            planilla.ingresar_leyenda(leyenda)
            planilla.ingresar_dias_laborados(dias_laborados)
            planilla.ingresar_cuenta(cuenta)
            planilla.clic_ingresar()
            planilla.clic_cerrar()
            print("Terminamos de registrar a ", modular)


if __name__ == '__main__':
    run()
