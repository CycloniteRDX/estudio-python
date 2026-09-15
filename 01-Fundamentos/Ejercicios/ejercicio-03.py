n_numeros = int(input('Introduce la cantidad de números: '))

suma_total = 0
positivo = 0
negativo = 0
ceros = 0

for index in range(n_numeros):
    numero = int(input(f'Introduce el numero {index+1}: '))
    if index == 0:
        mayor = numero
        menor = numero

    else:
        if numero > mayor:
            mayor = numero
        elif numero < menor:
            menor = numero

    suma_total += numero
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        ceros += 1

media = suma_total / n_numeros

print(f'Suma total: {suma_total}\nMedia: {media:.2f}\nMayor: {mayor}\nMenor: {menor}\nPositivos: {positivo}\nNegativos: {negativo}\nCeros: {ceros}')
            