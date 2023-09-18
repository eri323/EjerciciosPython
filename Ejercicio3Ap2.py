total_recaudado = 0
total_descuento = 0

personas = int(input("Ingrese la cantidad de personas a considerar: "))

for bn in range(personas):
    estrato = int(input("Ingrese el estrato (1 o 2): "))
    edad = int(input("Ingrese la edad: "))

    Descuento = 0

    if estrato == 1:
        if edad < 18:
            Descuento = 0.20
        else:
            Descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            Descuento = 0.10
        else:
            Descuento = 0.05
    valor_boleta = float(input("Ingrese el valor de la boleta: "))

    valor_descontado = valor_boleta * Descuento
    valor_a_pagar = valor_boleta - valor_descontado

    total_recaudado += valor_boleta
    total_descuento += valor_descontado

print(f"Total recaudado: {total_recaudado}")
print(f"Total descontado: {total_descuento}")