Conexion_a_internet = int(input("Digite la conexion en Mbps: "))
if Conexion_a_internet > 20:
  velocidad_de_descarga = "10 Mbps"
elif Conexion_a_internet < 20 and Conexion_a_internet > 5:
  velocidad_de_descarga = "5 Mbps"
elif Conexion_a_internet < 5:
  velocidad_de_descarga = "1 Mbps"

print("La velocidad de la descarga es:", velocidad_de_descarga, "debido a que la conexion internet es igual a:", Conexion_a_internet)