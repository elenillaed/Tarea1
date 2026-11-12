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


def main():


if __name__ == "__main__":
    main()