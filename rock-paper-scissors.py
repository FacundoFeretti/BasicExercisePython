jugador1 = input('Ingresa el nombre del jugador 1')
jugador2 = input('Ingresa el nombre del jugador 2')

eleccion1 = input(f'Hola, {jugador1} ¿Que eliges? ¿Piedra, Papel o tijeras? ')
eleccion2 = input(f'Hola, {jugador2} ¿Que eliges? ¿Piedra, Papel o tijeras? ')

condicion1 = eleccion1 == 'piedra' and eleccion2 == 'tijeras' 
condicion2 = eleccion1 == 'papel' and eleccion2 == 'piedra' 
condicion3 = eleccion1 == 'tijera' and eleccion2 == 'papel' 

if eleccion1 == eleccion2:
    print('Empate!')
elif(condicion1 or condicion2 or condicion3):
    print('Gana ', jugador1)
else:
    print('Gana', jugador2)