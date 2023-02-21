import planilla
import pandas as pd
import pyautogui


tiempo_inicio = 5
time_pass = 0.3

nombre_columnas = [
    'modular']

df = pd.read_csv("bd_baja_contrato.csv", names=nombre_columnas)

filas = len(df.axes[0])
columnas = len(df.axes[1])

modulares = []
decimas = []

print("\nCantidad de Registros: ", filas-1, "\n")
#print("Columnas: ", columnas)


def main():
    planilla.pausar(5)
    cantidad_registros = 0
    for i in range(len(df)):
        if i != 0:
            modular = df["modular"][i]
            #print("Comenzando a registrar a ", modular)
            planilla.buscar_modular(modular)
            planilla.abrir_habilitado()
            planilla.cambiar_situacion("5")
            decima = planilla.copiar_decima()
            decimas.append(decima)
            modulares.append(modular)
            planilla.clic_actualizar()
            planilla.clic_cerrar()
            print("copiar ", modular, ",", decima, ",", i, " de ", filas-1)
            cantidad_registros = cantidad_registros + 1

    print("Registros procesados: ", cantidad_registros, " \n")
    df_decimas = pd.DataFrame(list(zip(modulares, decimas)), columns=['Modular', 'Decimas'])
    print(df_decimas)
    df_decimas.to_csv('decimas.csv', index=False)


if __name__ == '__main__':
    main()
