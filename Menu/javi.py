import requests
import csv

def leer_empleados(nombre_archivo):
    empleados = []
    try:
        response = requests.get('https://raw.githubusercontent.com/JesusKu126/Examen/main/EMPLEADOS.txt')
        response.raise_for_status() 
        data = response.text.splitlines()
        reader = csv.reader(data)
        for row in reader:
            nombre, estado_civil, antiguedad, categoria, sueldo = row
            empleados.append((nombre, estado_civil, int(antiguedad), categoria, float(sueldo)))
    except requests.exceptions.RequestException as e:
        print(f"Error al leer el archivo desde el enlace: {e}")
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
    return empleados

def escribir_empleados(nombre_archivo, empleados):
    try:
        with open(nombre_archivo, 'w') as archivo:
            for empleado in empleados:
                archivo.write(','.join(map(str, empleado)) + '\n')
    except Exception as e:
        print(f"Error al escribir en el archivo {nombre_archivo}: {e}")

def merge_sort(empleados):
    if len(empleados) > 1:
        mid = len(empleados) // 2
        left_half = empleados[:mid]
        right_half = empleados[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                empleados[k] = left_half[i]
                i += 1
            else:
                empleados[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            empleados[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            empleados[k] = right_half[j]
            j += 1
            k += 1

def balanced_merge_sort(empleados):
    def natural_run_partition(empleados):
        if not empleados:
            return []

        runs = []
        new_run = [empleados[0]]
        for i in range(1, len(empleados)):
            if empleados[i][0] >= empleados[i-1][0]:
                new_run.append(empleados[i])
            else:
                runs.append(new_run)
                new_run = [empleados[i]]
        runs.append(new_run)
        return runs


nombre_archivo = 'EMPLEADOS.txt'
empleados = leer_empleados(nombre_archivo)

if empleados:
    merge_sort(empleados)
    escribir_empleados('EMPLEADOS_ordenados_mezcla_directa.txt', empleados)

    empleados = leer_empleados(nombre_archivo)

    balanced_merge_sort(empleados)
    escribir_empleados('EMPLEADOS_ordenados_mezcla_equilibrada.txt', empleados)

    print("Los empleados han sido ordenados y guardados en los archivos correspondientes.")
else:
    print("No se encontraron empleados para ordenar.")
