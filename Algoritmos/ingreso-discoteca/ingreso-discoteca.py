#1. Solicitar al usuario que ingrese la edad del cliente.

edad = int(input("Por favor ingresa tu edad: "))

#2. Verificar si al edad ingresada cumple con el requisito para entrar a la discoteca.

permitido = True if edad >= 18 else False #Ternario.

#3. Mostar al usuario si su cliente puede o no ingresar a la discoteca.

if permitido:
    print("Puedes ingresar a la discoteca!")
else: 
    print("Lo sentimos muicho, no se puede ingresar a la discooteca siendo menor de edad.")
