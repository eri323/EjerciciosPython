


import random



# Variables globales
lista_palabras = []
max_intentos = 6
palabra_actual = ""
palabra_oculta = []
letras_adivinadas = []
intentos = 0

def agregar_palabra():
    palabra = input("Ingresa una palabra para agregar al juego: ")
    lista_palabras.append(palabra)
    print(f'"{palabra}" ha sido agregada correctamente.')

def configurar():
    global max_intentos
    max_intentos = int(input("Ingresa el número de intentos permitidos: "))
    print(f'Número de intentos configurado a {max_intentos}.')

def seleccionar_palabra():
    global palabra_actual, palabra_oculta, intentos, letras_adivinadas
    palabra_actual = random.choice(lista_palabras).lower()
    palabra_oculta = ['_'] * len(palabra_actual)
    intentos = 0
    letras_adivinadas = []

def mostrar_palabra_oculta():
    print("Palabra a adivinar: " + " ".join(palabra_oculta))




def dibujar_ahorcado(max_intentos):
    partes_ahorcado = [
        "  _____",
        " |       |",
        " |       o",
        " |      -|-",
        " |       |",
        " |      //",
        " |"       
        "_|___"
    ]
    


    for linea in partes_ahorcado:
        print(linea)
    


def adivinar_letra():
    global intentos
    letra = input("Ingresa una letra: ").lower()

    if letra in letras_adivinadas:
        print(f'Ya has adivinado la letra "{letra}".')
        return

    letras_adivinadas.append(letra)

    if letra in palabra_actual:
        for i in range(len(palabra_actual)):
            if palabra_actual[i] == letra:
                palabra_oculta[i] = letra
    else:
        intentos += 1
        print(f'La letra "{letra}" no está en la palabra. Te quedan {max_intentos - intentos} intentos.')

def jugar():
    agregar_palabra()
    while True:
        print("\nMenú:")
        print("1. Agregar Palabra")
        print("2. Configurar")
        print("3. Jugar")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_palabra()
        elif opcion == "2":
            configurar()
        elif opcion == "3":
            seleccionar_palabra()
            while True:
                mostrar_palabra_oculta()
                adivinar_letra()
                if "_" not in palabra_oculta:
                    print("¡Felicidades! Has adivinado la palabra.")
                    
                    break
                elif intentos >= max_intentos:
                    print(f"Has perdido. La palabra era: {palabra_actual}")
                    dibujar_ahorcado(intentos)
                    break
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

jugar()
