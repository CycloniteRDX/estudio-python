# Ejercicio 08 — Menú de operaciones

Crea un programa que muestre un menú y permita al usuario realizar operaciones hasta que decida salir.

El menú debe mostrar estas opciones:

```text
1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Salir
```

El programa debe pedir una opción al usuario.

Si elige una operación, debe:

* Pedir dos números.
* Realizar la operación correspondiente.
* Mostrar el resultado.
* Volver a mostrar el menú.

Si elige `4`, el programa debe finalizar.

Si introduce una opción distinta de `1`, `2`, `3` o `4`, debe mostrar un mensaje indicando que la opción no es válida y volver a mostrar el menú.

## Restricciones

* Usa un bucle `while`.
* No uses `for`.
* No uses listas.
* No uses funciones.
* No uses librerías.
* Usa `if / elif / else`.
* No es necesario validar que los números introducidos sean realmente numéricos.

## Ejemplo de salida por consola

```text
1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Salir

Elige una opción: 1
Primer número: 5
Segundo número: 3
Resultado: 8

1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Salir

Elige una opción: 7
Opción no válida.

1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Salir

Elige una opción: 4
Programa finalizado.
```
