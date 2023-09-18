Estrato = int(input("Digite su estrato: "))
Edad = int(input("Digite su edad: "))
Matricula = 1000
if Estrato == 1 and Edad <18: 
  Matriculadesc = Matricula * 0.20
  MatriculaTotal = Matricula - Matriculadesc
elif Estrato == 1 and Edad >= 18: 
  Matriculadesc = Matricula * 0.15
  MatriculaTotal = Matricula - Matriculadesc
elif Estrato == 2 and Edad < 18: 
  Matriculadesc = Matricula * 0.10
  MatriculaTotal = Matricula - Matriculadesc
elif Estrato == 2 and Edad >= 18: 
  Matriculadesc = Matricula * 0.05
  MatriculaTotal = Matricula - Matriculadesc

print("El descuento que recibe es el siguiente: ",Matriculadesc)
print("Y el valor total a pagar seria:" ,MatriculaTotal)