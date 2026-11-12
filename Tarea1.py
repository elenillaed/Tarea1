import random

# 1. Definimos las constantes de las jugadas
PIEDRA = "piedra"
PAPEL = "papel"
TIJERAS  = "tijeras"

# 2. Función que decide quién gana
def decidir_ganador(user_action, computer_action):

    # Primero comprobamos si hay empate
    if user_action == computer_action:
        print("Usuario y ordenador eligieron", user_action, ". ¡Empate!")

    # Comprobamos si el usuario ha elegido piedra
    elif user_action == PIEDRA:
        if computer_action == TIJERAS:
            print("Piedra rompe tijeras. ¡Ganaste!")
        else:
            print("Papel envuelve piedra. ¡Perdiste!")

    # Comprobamos si el usuario ha elegido papel
    elif user_action == PAPEL:
        if computer_action == PIEDRA:
            print("Papel envuelve piedra. ¡Ganaste!")
        else:
            print("Tijeras cortan papel. ¡Perdiste!")

    # Comprobamos si el usuario ha elegido tijeras
    elif user_action == TIJERAS:
        if computer_action == PAPEL:
            print("Tijeras cortan papel. ¡Ganaste!")
        else:
            print("Piedra rompe tijeras. ¡Perdiste!")


# 3. Función principal del juego
def main():

    # Lista con las posibles jugadas
    opciones = [PIEDRA, PAPEL, TIJERAS]

    # Bucle para poder jugar varias rondas
    while True:

        # Pedimos al usuario que elija su jugada
        user_action = input(
            "\nElige una opción: piedra, papel o tijeras: "
        ).lower()

        # Comprobamos que la opción sea válida
        if user_action not in opciones:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        # El ordenador elige una jugada al azar
        computer_action = random.choice(opciones)

        # Mostramos las elecciones
        print("\nElegiste", user_action,
              ". El ordenador eligió", computer_action)

        # Llamamos a la función que decide quién gana
        decidir_ganador(user_action, computer_action)


if __name__ == "__main__":
    main()