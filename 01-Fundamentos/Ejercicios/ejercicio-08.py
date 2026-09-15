menu = ("1. Sumar dos números\n"
        "2. Restar dos números\n"
        "3. Multiplicar dos números\n"
        "4. Salir\n"
        "Introduce la opción deseada: ")

opcion = 0
while opcion != 4:
    opcion = int(input(menu))
    if opcion == 1:
        numero1 = int(input('Introduce el número 1: '))
        numero2 = int(input('Introduce el número 2: '))
        print(f'Resultado: {numero1 + numero2}')
    elif opcion == 2:
        numero1 = int(input('Introduce el número 1: '))
        numero2 = int(input('Introduce el número 2: '))
        print(f'Resultado: {numero1 - numero2}')
    elif opcion == 3:
        numero1 = int(input('Introduce el número 1: '))
        numero2 = int(input('Introduce el número 2: '))
        print(f'Resultado: {numero1 * numero2}')
    elif opcion == 4:
        pass
    else:
        print('Opcion invalida')