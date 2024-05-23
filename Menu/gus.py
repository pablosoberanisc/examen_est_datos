nombres = [
    "Carlos", "Andrea", "Luis", "Maria", "Jorge", "Ana", "Rafael", "Sofia", 
    "Juan", "Elena", "Pablo", "Isabel", "Miguel", "Lucia", "Fernando", "Carmen", 
    "Roberto", "Laura", "Sergio", "Patricia"
]
matriculas = [
    "A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", 
    "A009", "A010", "A011", "A012", "A013", "A014", "A015", "A016", 
    "A017", "A018", "A019", "A020"
]
num_materias_aprobadas = [
    3, 1, 5, 4, 3, 2, 2, 1, 
    1, 2, 8, 5, 6, 0, 2, 1, 
    4, 3, 1, 5
]
promedios = [
    8.1, 9.0, 7.8, 8.4, 7.9, 8.5, 9.2, 8.3, 
    6.7, 8.0, 8.6, 7.5, 8.2, 7.7, 9.1, 8.9, 
    7.4, 9.3, 8.7, 8.0
]

def seleccion_directa_por_nombre(nombres, matriculas, num_materias_aprobadas, promedios):
    n = len(nombres)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nombres[j] < nombres[min_idx]:
                min_idx = j
        nombres[i], nombres[min_idx] = nombres[min_idx], nombres[i]
        matriculas[i], matriculas[min_idx] = matriculas[min_idx], matriculas[i]
        num_materias_aprobadas[i], num_materias_aprobadas[min_idx] = num_materias_aprobadas[min_idx], num_materias_aprobadas[i]
        promedios[i], promedios[min_idx] = promedios[min_idx], promedios[i]

def quicksort(arr, indices):
    if len(arr) <= 1:
        return arr, indices
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    left_indices = [indices[i] for i in range(len(arr)) if arr[i] < pivot]
    middle_indices = [indices[i] for i in range(len(arr)) if arr[i] == pivot]
    right_indices = [indices[i] for i in range(len(arr)) if arr[i] > pivot]

    sorted_left, left_indices = quicksort(left, left_indices)
    sorted_right, right_indices = quicksort(right, right_indices)

    return sorted_left + middle + sorted_right, left_indices + middle_indices + right_indices

def ordenar_por_num_materias_aprobadas(nombres, matriculas, num_materias_aprobadas, promedios):
    indices = list(range(len(num_materias_aprobadas)))
    sorted_num_materias, sorted_indices = quicksort(num_materias_aprobadas, indices)
    
    nombres = [nombres[i] for i in sorted_indices]
    matriculas = [matriculas[i] for i in sorted_indices]
    promedios = [promedios[i] for i in sorted_indices]

    return nombres, matriculas, sorted_num_materias, promedios

print("Datos antes de ordenar:")
print("Nombres:", nombres)
print("Matrículas:", matriculas)
print("Número de materias aprobadas:", num_materias_aprobadas)
print("Promedios:", promedios)

seleccion_directa_por_nombre(nombres, matriculas, num_materias_aprobadas, promedios)
print("\nDatos ordenados por nombre (selección directa):")
print("Nombres:", nombres)
print("Matrículas:", matriculas)
print("Número de materias aprobadas:", num_materias_aprobadas)
print("Promedios:", promedios)

nombres, matriculas, num_materias_aprobadas, promedios = ordenar_por_num_materias_aprobadas(nombres, matriculas, num_materias_aprobadas, promedios)

print("\nDatos ordenados por número de materias aprobadas (Quicksort):")
print("Nombres:", nombres)
print("Matrículas:", matriculas)
print("Número de materias aprobadas:", num_materias_aprobadas)
print("Promedios:", promedios)
