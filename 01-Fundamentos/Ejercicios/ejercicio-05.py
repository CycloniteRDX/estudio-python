password = 'python123'
n_intentos = 0

while input('Introduce la contraseña: ') != password:
    print('Contraseña incorrecta')
    n_intentos += 1

print('Acceso concedido')
print(f'Número de intentos: {n_intentos+1}')