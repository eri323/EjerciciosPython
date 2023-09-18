""" # Pregunta con opciones múltiples

import random

Opciones = ["a","b","c"]


print("¡Escoje!")
print("a) Papel")
print("b) Piedra")
print("c) Tijera")

# Obtener la respuesta del usuario
respuesta = input("Elije una opción (a, b, c): ")

# Procesar la respuesta


def respuestaAleatoria():
    if respuesta in Opciones:
        respuesta_aleatoria = random.choice(Opciones)
        print(respuesta_aleatoria)

def Elije():
    while True:
        respuestaAleatoria()
        if respuesta == "a" and respuesta_aleatoria == "b":
            print("Ganaste")
            break
            print("Tu color favorito es Rojo.")
        elif respuesta == "b":
            print("Tu color favorito es Azul.")
        elif respuesta == "c":
            print("Tu color favorito es Verde.")
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (a, b, c, d).")


 """


import random

opciones = ["a", "b", "c"]

def respuestaAleatoria():
    return random.choice(opciones)

def Elije():
    while True:
        
        respuesta = input("Elije una opción (a, b, c): ")
        respuesta_aleatoria = respuestaAleatoria()

        print(f"Tu elección: {respuesta}")
        print(f"Elección aleatoria: {respuesta_aleatoria}")

        if respuesta == respuesta_aleatoria:
            print("Empate")
        elif respuesta == "b" and respuesta_aleatoria == "c":
            print("Ganaste")
            break
        elif respuesta == "c" and respuesta_aleatoria == "a":
            print("Ganaste")
            break
        elif respuesta == "a" and respuesta_aleatoria == "b":
            print("Ganaste")
            break
        else:
            print("Perdiste")
            break

        


print("¡Escoje!")
print("a) Papel")
print("b) Piedra")
print("c) Tijera")       



Elije()
