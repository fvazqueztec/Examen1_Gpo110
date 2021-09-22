![Tec de Monterrey](../../images/logotecmty.png)
# Interés mensual

Escribe un programa que reciba:
* Un número decimal que indique el monto a invertir
* Un número decimal que indique el interes ANUAL
* Un número entero que represente el número de meses que será invertido el monto. 

El programa deberá: 
* Calcular el interés mensual
* Cada mes, se debe calcular el nuevo interés con el monto acumulado. 

Por ejemplo, para las siguientes entradas: 
Monto: 1000
Interés anual: 12
Meses: 3

El interes mensual corresponde al 1%, por lo que:
* En el mes número 1, se ganó 10 pesos de intereses por lo que el nuevo monto es de 1010 
* En el mes número 2, se ganó 10.1 pesos de intereses por lo que el nuevo monto es de 1020.1 
* En el mes número 3, se ganó 10.201 pesos de intereses por lo que el nuevo monto es de 1030.301

El programa deberá entregar la cantidad redondeada a 2 decimales, para el ejemplo anterior, deberá entregar 1030.3 (recuerda utilizar la instrucción  round(cantidad, 2)  )

Si cualquiera de los valores es negativo o cero, se debe indicar el mensaje de "Error en los datos"

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():    
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

La salida del programa debe de ser solamente el resultado, sin leyendas ni mensajes, debe ser de la siguiente forma:


```
Monto: 55.23
Interés anual: 12.5
Meses: -2
Error en los datos
```

```
Monto: 0
Interés anual: 20.34
Meses: 3
Error en los datos
```

```
Monto: 1000
Interés anual: 12
Meses: 3
1030.3
```


```
Monto: 5534.23
Interés anual: 8.9
Meses: 5
5742.52
```


**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

