suma = 0
cantidad_pares = 0
cantidad_impares = 0
numero_menor = None
numero_mayor = None




while True:
    numero = float(input("Digte numeros: "))
    if numero <0:
        break
    suma += numero

    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    if numero_menor is None or numero < numero_menor:
        numero_menor = numero
    if numero_mayor is None or numero > numero_mayor:
        numero_mayor = numero


print(f"Sumatoria de los números: {suma}")
print(f"Cantidad de números pares:  {cantidad_pares}")
print(f"Cantidad de números impares:  {cantidad_impares}")
print(f"Número menor: {numero_menor}")
print(f"Número mayor: {numero_mayor}")