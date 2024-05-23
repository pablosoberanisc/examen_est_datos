def quicksort_hoteles(hoteles, low, high):
    if low < high:
        pi = particion(hoteles, low, high)
        quicksort_hoteles(hoteles, low, pi - 1)
        quicksort_hoteles(hoteles, pi + 1, high)

def particion(hoteles, low, high):
    pivote = hoteles[high]
    i = low - 1

    for j in range(low, high):
        if (hoteles[j]["Ciudad"], hoteles[j]["Nombre de Hotel"]) < (pivote["Ciudad"], pivote["Nombre de Hotel"]):
            i += 1
            hoteles[i], hoteles[j] = hoteles[j], hoteles[i]

    hoteles[i + 1], hoteles[high] = hoteles[high], hoteles[i + 1]
    return i + 1


hoteles = [
    {"Nombre de Hotel": "EROS", "Ciudad": "Merida", "Número de estrellas": 5, "Número de cuartos": 100},
    {"Nombre de Hotel": "EROS 2", "Ciudad": "Barcelona", "Número de estrellas": 5, "Número de cuartos": 200},
    {"Nombre de Hotel": "SEÑORIAL EXPRESS", "Ciudad": "Madrid", "Número de estrellas": 3, "Número de cuartos": 150},
    {"Nombre de Hotel": "DESEO REAL", "Ciudad": "Progreso", "Número de estrellas": 2, "Número de cuartos": 120},
    {"Nombre de Hotel": "MARACAY", "Ciudad": "Sevilla", "Número de estrellas": 3, "Número de cuartos": 80}
]

quicksort_hoteles(hoteles, 0, len(hoteles) - 1)

for hotel in hoteles:
    print(f"Nombre de Hotel: {hotel['Nombre de Hotel']}, Ciudad: {hotel['Ciudad']}, "
          f"Número de estrellas: {hotel['Número de estrellas']}, Número de cuartos: {hotel['Número de cuartos']}")
