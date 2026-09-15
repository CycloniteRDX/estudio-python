n_mediciones = int(input('Ingrese el número de mediciones: '))
lista_temperaturas = []

for i in range(n_mediciones):
    temperatura = float(input(f'Temperatura {i+1}: '))
    lista_temperaturas.append(temperatura)

print(lista_temperaturas)
for valor in lista_temperaturas:
    print(f'Temperatura: {valor} ºC')
print(f'Número de temperaturas: {len(lista_temperaturas)}')
