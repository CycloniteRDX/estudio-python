# Ejercicio 01 — Consumo eléctrico

Crea un programa que calcule el consumo eléctrico de un dispositivo.

El usuario debe introducir los siguientes datos:

* Tensión en voltios.
* Corriente en amperios.
* Horas de funcionamiento.
* Precio de la electricidad en €/kWh.

El programa debe calcular y mostrar:

* Potencia en vatios.
* Energía consumida en kWh.
* Coste total de funcionamiento.

Además, debe clasificar el consumo según la potencia:

* Menos de 100 W → `Consumo bajo`
* Entre 100 W y 1000 W → `Consumo medio`
* Más de 1000 W → `Consumo alto`

## Restricciones

* Usa `input()` para leer los datos.
* Convierte las entradas al tipo adecuado.
* Usa variables con nombres claros.
* Usa una estructura `if / elif / else`.
* No uses funciones.
* No uses librerías.
* No es necesario validar entradas incorrectas.

## Ejemplo de salida por consola

```text
Tensión (V): 230
Corriente (A): 0.5
Horas de funcionamiento: 8
Precio de la electricidad (€/kWh): 0.18

Potencia: 115.0 W
Energía: 0.92 kWh
Coste: 0.17 €
Consumo medio
```
