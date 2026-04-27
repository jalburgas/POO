
  # archivo: insertar_pokemon.py

from class_pokemon import Pokemon, Pikachu, Charmander

def main():
    print("=== INSERTAR POKEMON ===")
    
    print("\n1. Pokemon básico")
    print("2. Pikachu")
    print("3. Charmander")
    
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
        return
    
    print("\n--- POKEMON CREADO ---")
    pokemon.descripcion()
    
    if isinstance(pokemon, Pikachu):
        print(pokemon.ataque())

if __name__ == "__main__":
    main()              
   
