# 1. Solicitar al usuario las medidas de la pieza del mueble en cms.

medida_cm = float(input("Por favor, ingresar las medidas de la pieza del mueble (en cms): "))

# 2. Convertir las medidas de centimetros a pulgadas.

medida_pulgada = medida_cm / 2.54

# 3. Mostrar las medidas convertidas en pulgadas al usuario.

print(f"La medida en pulgadas de la pieza ingresada es: {medida_pulgada}")