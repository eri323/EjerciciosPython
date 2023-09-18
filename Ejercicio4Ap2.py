import random

lanzamientos_totales = 0
lanzamientos_sin_uno = 0

while lanzamientos_totales < 10:
    lanzamiento = random.randint(1, 6)
    lanzamientos_totales += 1

    print(f"Lanzamiento {lanzamientos_totales}: {lanzamiento}")

    if lanzamiento == 1:
        lanzamientos_sin_uno = 0
        print("¡Has sacado un 1! Has perdido.")
        break
    else:
        lanzamientos_sin_uno += 1

    if lanzamientos_sin_uno == 10:
        print("¡Has ganado! Has lanzado 10 veces sin sacar un 1.")
        break
