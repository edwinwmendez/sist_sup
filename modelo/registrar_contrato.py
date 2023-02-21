import pandas as pd

def leer_csv(self):
    # Obtener el nombre del archivo CSV seleccionado por el usuario
    nombre_archivo = self.ventana_principal.obtener_nombre_archivo()

    # Leer el archivo CSV y cargar los datos en un DataFrame
    df = pd.read_csv(nombre_archivo)

    # Imprimir los primeros 5 registros del DataFrame para verificar que los datos se hayan leído correctamente
    print(df.head())

    # Realizar otras operaciones en los datos, si es necesario
