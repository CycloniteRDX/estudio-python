n_mediciones = int(input('Introduce el número de mediciones: '))
print('Ahora introduce el valor de las mediciones')

medicion = 0
min = 0
max = 0
media = 0
suma_medicion = 0
for n in range(n_mediciones):
    medicion = float(input(f'Introduce el valor de la medicion {n+1}: '))
    suma_medicion += medicion

    if medicion > max:
        max = medicion
    if medicion < min:
        min = medicion
    media = suma_medicion / n_mediciones

print(f'Temperatura media: {media:.2f}\nTemperatura max: {max:.2f}\nTemperatura min: {min:.2f}\nNúmero de mediciones: {n_mediciones}')

