numero = int(input("Ingrese un numero entero positivo: "))

print('Números encontrados: ', end = " ")
n_divisores = 0
for i in range(1,numero+1): # se suma 1 a número porque empezamos el range en 1, no en 0
    if numero % i == 0:
        print(i, end = " ")
        n_divisores += 1

print(f'\nNúmero de divisores: {n_divisores}')
if n_divisores == 2:
    print(f'El número {numero} es primo')
else:
    print(f'El número {numero} no es primo')
