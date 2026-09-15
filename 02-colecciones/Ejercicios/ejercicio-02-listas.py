n_numeros = int(input('Cuántos números quieres introducir: '))
lista_numeros = []
suma = 0
positivos = 0
negativos = 0
ceros = 0

for i in range(n_numeros):
    numero = float(input(f'Introduce el número {i+1}: '))
    lista_numeros.append(numero)

for index,valor in enumerate(lista_numeros):
    if index == 0:
        mayor = valor
        menor = valor
    else:
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor

    suma += valor
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    else:
        ceros += 1

media = suma/n_numeros

print(f'Lista: {lista_numeros}')
print(f'Mayor: {mayor}')
print(f'Menor: {menor}')
print(f'Suma: {suma}')
print(f'Media: {media:.2f}')
print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')
print(f'Ceros: {ceros}')