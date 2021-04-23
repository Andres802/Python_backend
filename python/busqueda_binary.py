import time

objetivo = int(input('Escoge un numero: '))
epsilon = 0.000001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo)/2
num = 0 #numero para contar iteraciones

start = time.time()

while abs(respuesta**2 - objetivo) >= epsilon:

    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo)/2

    num += 1

end = time.time()

print(f'Para resolver hizo {num} iteraciones y se demoro {end - start} segundos')

print(f'La raiz cuadrada de {objetivo} es {respuesta}')