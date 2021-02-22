def run():
    
    nombre_1 = input('Ingrese primer nombre: ')
    edad_1 = int(input('Ingrese edad de {nombre_1}: '))

    nombre_2 = input('Ingrese segundo nombre: ')
    edad_2 = int(input('Ingrese edad de {nombre_2}: '))

    if edad_1 > edad_2:
        print("{:s}".format(nombre_1), 'es el mayor con '+ str(edad_1) + ' años')
    elif edad_1 < edad_2:
        print("{:s}".format(nombre_1), 'es el mayor con ' + str(edad_2) + ' años')
    else:
        print("{:s} y {:s}".format(nombre_1, nombre_2), 'tienen la misma edad')


if __name__ == '__main__':
    run()