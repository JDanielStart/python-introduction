'''
Example of solution approximation algorithm
Epsilon will have greater precision if we seek a more exact answer
and epsilon will have less precision when we seek speed instead of
a more exact answer.
'''

objetivo = int(input('Escoge un número: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) > epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo))
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la ríz cuadrada del {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
