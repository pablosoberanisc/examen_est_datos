import os

def mostrar_menu():
    print("Menú:")
    print("1. Chuy")
    print("2. Dani")
    print("3. Gus")
    print("4. Javi")
    print("5. Pablo")
    print("6. Salir")

def ejecutar_programa(nombre_programa):
    try:
        os.system(f"python {nombre_programa}.py")
    except FileNotFoundError:
        print(f"Error: El programa {nombre_programa}.py no fue encontrado.")
    except Exception as e:
        print(f"Error al ejecutar el programa {nombre_programa}: {e}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número correspondiente al programa que desea ejecutar: ")

        if opcion == '1':
            ejecutar_programa("chuy")
        elif opcion == '2':
            ejecutar_programa("dani")
        elif opcion == '3':
            ejecutar_programa("gus")
        elif opcion == '4':
            ejecutar_programa("javi")
        elif opcion == '5':
            ejecutar_programa("pablo")
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 6.")

if __name__ == "__main__":
    main()
