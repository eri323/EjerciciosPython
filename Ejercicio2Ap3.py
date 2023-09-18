Frase1 = input("Ingrese la primera frase: ")
Frase2 = input("Ingrese la segunda frase: ")

min_length = min(len(Frase1), len(Frase2))
Frase1 = Frase1[:min_length]
Frase2 = Frase2[:min_length]

Letras_R = []

for i in range(min_length):
    if Frase1[i] == Frase2[i]:
        Letras_R.append(Frase1[i])

print("Letras repetidas en la misma posición:")
print(Letras_R)
