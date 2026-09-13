n_numeros = int(input('Introduce la cantidad de números: '))

for index in range(n_numeros):
    numero = int(input(f'Introduce el numero {index+1}: '))
    if index == 0:
        suma_total = numero
        mayor = numero
        menor = numero
        if numero > 0:
            positivo = 1
            negativo = 0
            ceros = 0
        if numero < 0:
            negativo = 1
            positivo = 0
            ceros = 0
        if numero == 0:
            ceros = 1
            positivo = 0
            negativo = 0
    else:
        suma_total += numero
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
        if numero > 0:
            positivo += 1
        if numero < 0:
            negativo += 1
        if numero == 0:
            ceros += 1

media = suma_total / n_numeros

print(f'Suma total: {suma_total}\nMedia: {media:.2f}\nMayor: {mayor}\nMenor: {menor}\nPositivos: {positivo}\nNegativos: {negativo}\nCeros: {ceros}')
            