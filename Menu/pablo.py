import pandas as pd

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

url_A1 = "https://raw.githubusercontent.com/pablosoberanisc/examen_est_datos/main/A1_1.csv"
url_A2 = "https://raw.githubusercontent.com/pablosoberanisc/examen_est_datos/main/A2_1.csv"
url_A3 = "https://raw.githubusercontent.com/pablosoberanisc/examen_est_datos/main/A3_1.csv"

df_A1 = pd.read_csv(url_A1)
df_A2 = pd.read_csv(url_A2)
df_A3 = pd.read_csv(url_A3)

df_recitales = pd.concat([df_A1, df_A2, df_A3])

nombres = df_recitales['Nombre'].tolist()
burbuja(nombres)

presentaciones_ordenadas = df_recitales.set_index('Nombre').loc[nombres]['Presentaciones'].tolist()
fechas_ordenadas = df_recitales.set_index('Nombre').loc[nombres]['Fechas'].tolist()

df_recitales_ordenados = pd.DataFrame({'Nombre': nombres, 'Presentaciones': presentaciones_ordenadas, 'Fechas': fechas_ordenadas})

df_recitales_ordenados.to_csv('recitales.csv', index=False)

print("Archivo 'recitales.csv' creado exitosamente con los datos ordenados.")

