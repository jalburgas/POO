# archivo: insertar_pokemon.py

from class_pokemon import Pokemon, Pikachu, Charmander

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Insertar Pokemon")
        print("2. Salir")
        
        opcion_menu = input("\nElige una opción (1-2): ")
        
        if opcion_menu == "2":
            print("¡Hasta luego! Saliendo del programa...")
            break
        
        elif opcion_menu == "1":
            print("\n=== INSERTAR POKEMON ===")
            
            print("\n1. Pokemon básico")
            print("2. Pikachu")
            print("3. Charmander")
            
            try:
                opcion = int(input("\nElige una opción (1-3): "))
                nombre = input("Nombre del Pokemon: ")
                tipo = input("Tipo del Pokemon: ")
                
                if opcion == 1:
                    pokemon = Pokemon(nombre, tipo)
                elif opcion == 2:
                    pokemon = Pikachu(nombre, tipo)
                elif opcion == 3:
                    pokemon = Charmander(nombre, tipo)
                else:
                    print("Opción no válida")
                    continue
                
                print("\n--- POKEMON CREADO ---")
                pokemon.descripcion()
                
                if isinstance(pokemon, Pikachu):
                    print(pokemon.ataque())
                    
            except ValueError:
                print("Error: Por favor ingresa un número válido")
        else:
            print("Opción no válida. Por favor elige 1 o 2.")

if __name__ == "__main__":
    main()
   
