from recetas import receta_pasta
from recetas import receta_costillas_kanka,receta_tacos
from recetas import receta_tornillosape
# Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("2. Costillas al kanka")
    print("3. Tacos")
    print("5. Tornillos")
    # Agrega aquí tu receta con un número nuevo

    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    elif opcion=='2':
        receta_costillas_kanka()
    elif opcion=='3':
        receta_tacos()
    elif opcion=='5':
        receta_tornillosape()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
