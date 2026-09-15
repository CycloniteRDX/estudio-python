n_numeros = 0
suma_numeros = 0
media_numeros = 0
numero_introducido = int(input("Introduce un numero: "))

while numero_introducido != 0:
    n_numeros += 1
    suma_numeros += numero_introducido
    numero_introducido = int(input("Introduce un numero: "))

if n_numeros > 0:
    media_numeros = (suma_numeros / n_numeros)
print(f'Suma total: {suma_numeros}')
print(f'Cantidad de números: {n_numeros}')
print(f'Media: {media_numeros:.2f}')