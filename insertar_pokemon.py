# archivo: insertar_pokemon.py

from class_pokemon import Pokemon, Pikachu, Charmander

def insertar_pokemon():
    print("=== INSERTAR NUEVO POKEMON ===")
    
    print("\nTipos de Pokemon disponibles:")
    print("1. Pokemon básico")
    print("2. Pikachu")
    print("3. Charmander")
    
    try:
        opcion = int(input("\nSelecciona el tipo de Pokemon (1-3): "))
        
        nombre = input("Nombre del Pokemon: ")
        tipo = input("Tipo del Pokemon: ")
        
        if opcion == 1:
            nuevo_pokemon = Pokemon(nombre, tipo)
            print(f"\n✅ Pokemon '{nombre}' creado exitosamente!")
            nuevo_pokemon.descripcion()
            
        elif opcion == 2:
            nuevo_pokemon = Pikachu(nombre, tipo)
            print(f"\n✅ Pikachu '{nombre}' creado exitosamente!")
            nuevo_pokemon.descripcion()
            print(nuevo_pokemon.ataque())
            
        elif opcion == 3:
            nuevo_pokemon = Charmander(nombre, tipo)
            print(f"\n✅ Charmander '{nombre}' creado exitosamente!")
            nuevo_pokemon.descripcion()
            
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Error: Debes ingresar un número válido")
    except Exception as e:
        print(f"❌ Error al insertar Pokemon: {e}")

def insertar_varios_pokemon():
    print("=== INSERTAR MÚLTIPLES POKEMON ===")
    lista_pokemon = []
    
    while True:
        print("\n--- Nuevo Pokemon ---")
        insertar_pokemon()
        
        continuar = input("\n¿Deseas insertar otro Pokemon? (s/n): ").lower()
        if continuar != 's':
            break
    
    print(f"\n✅ Total de Pokemon insertados correctamente")

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Insertar un Pokemon")
    print("2. Insertar múltiples Pokemon")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-3): "))
            
            if opcion == 1:
                insertar_pokemon()
            elif opcion == 2:
                insertar_varios_pokemon()
            elif opcion == 3:
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida")
                
        except ValueError:
            print("❌ Error: Debes ingresar un número")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
