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

oportunidades = int(input("¿Cuántas veces desea jugar?: "))
ganadasmias = 0
ganadasmaquina = 0
contador = 0



def Elije():
    global contador, ganadasmias, ganadasmaquina
    while True:
        respuesta = input("Elije una opción (a, b, c): ")
        respuesta_aleatoria = respuestaAleatoria()
    
        print(f"Tu elección: {respuesta}")
        print(f"Elección aleatoria: {respuesta_aleatoria}")

        if respuesta == respuesta_aleatoria:
            print("Empate")
            contador += 1
        elif respuesta == "b" and respuesta_aleatoria == "c":
            print("Ganaste")
            contador += 1
            ganadasmias += 1
        elif respuesta == "c" and respuesta_aleatoria == "a":
            print("Ganaste")
            contador += 1
            ganadasmias += 1
        elif respuesta == "a" and respuesta_aleatoria == "b":
            print("Ganaste")
            contador += 1
            ganadasmias += 1
        else:
            print("Perdiste")
            contador += 1
            ganadasmaquina += 1

       

        
        if contador == oportunidades: 
            if ganadasmias > ganadasmaquina: 
                print(f"Haz ganado el juego con un total de {ganadasmias} a {ganadasmaquina}")
                break
            elif ganadasmias == ganadasmaquina: 
                print(f"Juego empatado")
                break
            else:
                print(f"Haz perdido el juego con un total de {ganadasmaquina} a {ganadasmias}")
                break
           
        
      
        


print("¡Escoje!")
print("a) Papel")
print("b) Piedra")
print("c) Tijera")       



Elije()
