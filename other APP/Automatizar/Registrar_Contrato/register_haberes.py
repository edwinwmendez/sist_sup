import planilla
import pandas as pd
import pyautogui
from colorama import init, Fore, Style, Back

# Para iniciar colorama
init()

tiempo_inicio = 5
time_pass = 0.3

nombre_columnas = [
    'modular',
    'reinman_af',
    'reinman_no_af']

df = pd.read_csv("bd_register_haberes.csv", names=nombre_columnas)

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
            reinman_af = df["reinman_af"][i]
            reinman_no_af = df["reinman_no_af"][i]
            #print("Comenzando a registrar a ", modular)
            planilla.buscar_modular(modular)
            planilla.seleccionar_registro()
            #planilla.abrir_habilitado()
            planilla.abrir_haberes()
            planilla.agregar_haber("92",reinman_af)
            planilla.agregar_haber("99", reinman_no_af)
            planilla.cerrar_haberes()
            #planilla.ingresar_leyenda_mensual()
            planilla.clic_actualizar()
            planilla.clic_cerrar()            
            print(Fore.GREEN +"INFO> \t ", Fore.RESET +"Procesado a ", end=""),
            print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + " " + modular, Fore.RESET + Style.RESET_ALL + "--->", i, "de", filas-1)
            cantidad_registros = cantidad_registros + 1

    print("Registros procesados: ", cantidad_registros, " \n")
    #df_decimas = pd.DataFrame(list(zip(modulares, decimas)), columns=['Modular', 'Decimas'])
    #print(df_decimas)
    #df_decimas.to_csv('decimas.csv', index=False)


if __name__ == '__main__':
    main()