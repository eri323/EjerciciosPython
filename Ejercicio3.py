CalParcial1 = int(input("Calificacion del parcial 1 : "))
CalParcial2  = int(input("Calificacion del parcial 2 : "))
CalParcial3 = int(input("Calificacion del parcial 3 : "))
ExamenFinal = int(input("Calificacion del examen fianl : "))
TrabajoFinaal  = int(input("Calificacion del trabajo final : "))

CalParciales= (CalParcial1 + CalParcial2 + CalParcial3) / 3 
CalParcialesPor = CalParciales * 0.55

ExamenFinalPor = ExamenFinal * 0.30

TrabajoFinalPor = TrabajoFinaal * 0.15
CalFinal = CalParcialesPor + TrabajoFinalPor + ExamenFinalPor
print("La calificacion final en la materia de matematicas es: ", CalFinal)