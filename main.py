import random


def inicio():
    titulo = "BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO"
    print(f"\n {titulo}")
    print("-" * len(titulo))
    input("Pulsa una tecla para continuar... ")

    intentos = dificultad()
    numero_secreto = generar_num()
    pedir_intento(intentos, numero_secreto)


def generar_num():
    return random.randint(1, 100)


def dificultad():
    print("Tipos de dificultad: \n")
    print("""
    1. Fácil (10 intentos)
    2. Medio (5 intentos)
    3. Difícil (3 intentos)
    """)

    while True:
        try:
            opcion = int(input("Elige la dificultad (1-3): "))
            if opcion == 1:
                return 10
            elif opcion == 2:
                return 5
            elif opcion == 3:
                return 3
            else:
                print("Opción no válida. Elige entre 1-3")
        except ValueError:
            print("Debes introducir un numero...")


def pedir_intento(intentos, numero_secreto):
    while intentos > 0:
        try:
            intento = int(input(f"Te quedan {intentos} intento/s. Adivina el numero del 1 al 100: "))

            if intento == numero_secreto:
                print("Has adivinado el numero secreto")
            elif intento > numero_secreto:
                print("El numero secreto es menor")
            elif intento < numero_secreto:
                print("El numero secreto es mayor")

            intentos -= 1

            if intentos <= 0 and intento != numero_secreto:
                print(f"Has fallado! El numero secreto era {numero_secreto}")

        except ValueError:
            print("Introduce un numero válido.")


def main():
    inicio()


if __name__ == "__main__":
    main()