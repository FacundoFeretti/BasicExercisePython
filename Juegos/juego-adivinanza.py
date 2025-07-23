import random

numero_secreto = random.randint(0,100)
adivinado = False
cant_intentos = 0

print('Guess the number game!')

while not adivinado:
    if not cant_intentos < 5:
        print('Game Over! No has podido adivinar el numero dentro de los 5 intentos!')
        break
    numero = int(input('Introduce un numero del 1 al 99: '))

    if numero == numero_secreto:
        print('Felicitaciones has adivinado el numero secreto!')
        adivinado= True
    elif numero < numero_secreto:
        print('El numero es mayor al ingresado')
    else:
        print('El numero es menor al ingresado')
    cant_intentos += 1
