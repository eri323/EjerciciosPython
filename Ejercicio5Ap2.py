PasswordCorrecto = "Eri"

Intentos = 0

while Intentos < 5:
    PasswordIngresado = input("Digite la password: ")

    if PasswordIngresado == PasswordCorrecto:
        print("Acceso permitido")
        break

    print("Password Incorrecta")
    Intentos += 1

if Intentos == 5:
    print("No puede volver a intentarlo despues de 5 veces")