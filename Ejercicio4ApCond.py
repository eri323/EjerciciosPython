Nhemoglobina = float(input("Digite su nivel de Hemoglobina: "))
Edad = float(input("Digite su edad, en caso de que sea menor de un año digite de la siguiente manera(0.1 = 1 mes, 0.2=2meses y asi sucesivamente): "))
Sexo = input("Digite su sexo(M=Masculino y F=Femenino): ")

if Edad > 0 or Edad <= 0.1 and Nhemoglobina <13 :
    Anemia = "Positivo"
elif Edad > 0.1 and Edad <= 0.6 and Nhemoglobina <10 :
    Anemia = "Positivo"
elif Edad > 0.6 and Edad <= 1 and Nhemoglobina <11 :
    Anemia = "Positivo"
elif Edad >1 and Edad <= 5 and Nhemoglobina <11.5 :
    Anemia = "Positivo"
elif Edad >5 and Edad <= 10 and Nhemoglobina <12.6 :
    Anemia = "Positivo"
elif Edad >10 and Edad <= 15 and Nhemoglobina <13 :
    Anemia = "Positivo"
elif Edad >15 and Nhemoglobina <12 and Sexo == F :
    Anemia = "Positivo"
elif Edad >15 and Nhemoglobina <14 and Sexo == M :
    Anemia = "Positivo"
else:
    Anemia= "Negativo"

print("Su estado de anemia es: ",Anemia)