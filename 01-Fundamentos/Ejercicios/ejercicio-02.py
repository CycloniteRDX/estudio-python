n_mediciones = int(input('Introduce el número de mediciones: '))
print('Ahora introduce el valor de las mediciones')


suma_medicion = 0
for n in range(n_mediciones):
    medicion = float(input(f'Introduce el valor de la medicion {n + 1}: '))

    if n == 0: # si estamos en la primera medicion/valor, inicializamos variables
        minimo = medicion
        maximo = medicion

    else:

        if medicion > maximo:
            maximo = medicion
        if medicion < minimo:
            minimo = medicion

    suma_medicion += medicion

media = suma_medicion / n_mediciones

print(f'Temperatura media: {media:.2f}\nTemperatura max: {maximo:.2f}\nTemperatura min: {minimo:.2f}\nNúmero de mediciones: {n_mediciones}')

