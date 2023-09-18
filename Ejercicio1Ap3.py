N_Elementos = int(input("Ingrese la cantidad de elementos que desea en la lista: "))

Lista = []


for i in range(N_Elementos):
    Elemento = input(f"Ingrese el elemento {i + 1}: ")
    Lista.append(Elemento)

print("Lista original:")
print(Lista)


Lista_invertida = Lista[::-1]


print("Lista invertida:")
print(Lista_invertida)
