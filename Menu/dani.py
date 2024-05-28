class Alumno:
    def __init__(self, nombre, promedio, materias_aprobadas):
        self.nombre = nombre
        self.promedio = promedio
        self.materias_aprobadas = materias_aprobadas

    def __str__(self):
        return f"Nombre: {self.nombre}, Promedio: {self.promedio}, Materias Aprobadas: {self.materias_aprobadas}"

def ingresar_alumnos():
    alumnos = []
    n = int(input("Ingrese el número de alumnos: "))
    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        promedio = float(input(f"Ingrese el promedio de {nombre}: "))
        materias_aprobadas = int(input(f"Ingrese el número de materias aprobadas por {nombre}: "))
        alumnos.append(Alumno(nombre, promedio, materias_aprobadas))
    return alumnos

def buscar_alumno(alumnos, nombre_buscado):
    for alumno in alumnos:
        if alumno.nombre == nombre_buscado:
            return alumno
    return None

def main():
    print("Ingrese los datos de los alumnos:")
    alumnos = ingresar_alumnos()

    alumnos.sort(key=lambda x: x.promedio, reverse=True)

    nombre_buscado = input("Ingrese el nombre del alumno a buscar: ")

    print("\nLista de alumnos ordenados por promedio:")
    for alumno in alumnos:
        print(alumno)

    alumno_encontrado = buscar_alumno(alumnos, nombre_buscado)

    if alumno_encontrado:
        print("\nAlumno encontrado:")
        print(alumno_encontrado)
    else:
        print("\nAlumno no encontrado.")

if __name__ == "__main__":
    main()
