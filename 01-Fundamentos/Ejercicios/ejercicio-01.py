tension_v = float(input('Introduce la tensión de la máquina: '))
corriente_a = float(input('Introduce la corriente de la máquina: '))
tiempo_h = float(input('Introduce el tiempo de funcionamiento de la máquina (h): '))
precio_ekwh = float(input('Introduce el precio de la electricidad (€/kWh)'))

potencia = tension_v * corriente_a
energia = (potencia / 1000) * tiempo_h
coste = energia * precio_ekwh

if potencia < 100:
    consumo = 'bajo'
elif potencia <= 1000: #se puede poner potencia entre 100 y 1000, pero si python ha llegado a este elif ya sabe que la potencia es mayor que 100, por lo tanto podemos omitirlo
    consumo = 'medio'
else:
    consumo = 'alto'

print(f'Tensión (V): {tension_v}\nCorriente (A): {corriente_a}\nHoras de funcionamiento (h): {tiempo_h}\nPrecio de la electricidad (€/kWh): {precio_ekwh}')
print(f'Potencia: {potencia:.2f} W\nEnergía: {energia:.2f} kWh\nCoste: {coste:.2f} €\nConsumo: {consumo}')