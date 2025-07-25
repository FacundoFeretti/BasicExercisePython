import math

#1. Solicite al usuario que ingrese el radio del circulo.

radio = float(input("Ingrese el radio del circulo: "))

#2. Calcular el area del circulo utilizando formula area = π * radioɅ2

area = math.pi * (radio**2)

#3. Mostrar al usuario el area calculada.

print("El area del circulo con radio: ", radio, "es: ", area)