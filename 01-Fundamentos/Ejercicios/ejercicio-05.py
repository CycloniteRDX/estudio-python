password = 'python123'
pass_introducida = ""
n_intentos = 0

while pass_introducida != password:
    pass_introducida = input('Introduce la contraseña: ')
    n_intentos += 1
    if pass_introducida != password:
        print('Contraseña incorrecta')

print('Acceso concedido')
print(f'Número de intentos: {n_intentos}')