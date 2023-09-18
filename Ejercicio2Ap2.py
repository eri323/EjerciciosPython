numero = int(input("Ingrese un número para la tabla de multiplicar: "))

for i in range (1 , 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")