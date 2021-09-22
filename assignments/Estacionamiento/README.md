![Tec de Monterrey](../../images/logotecmty.png)
# Estacionamiento

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe aquí tu código
    

if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  

El siguiente algoritmo se puede usar para determinar la cantidad a pagar en un estacionamiento, considerando lo siguiente:

   * Solicitar la cantidad de horas, si la cantidad de horas es menor que cero, el sistema deberá terminar y mostrar el mensaje "Error en los datos" 
   * Solicitar los minutos, si la cantidad de minutos es menor que cero o mayor que 60, el sistema deberá terminar y mostrar el mensaje "Error en los datos" 
   * El costo de la primera hora o fracción de hora es de 10 pesos. 
   * A partir de la segunda hora, se cobra cada fracción de 15 minutos o menos a 2 pesos, es decir, 8 pesos la hora. 
   
**Entradas**  
Horas
Minutos (solo si Horas es mayor o igual que 0)

  
**Salidas**  
Si las Horas es menor que cero, deberá mostrar el siguiente mensaje: 
    **Error en los datos**
Si los minutos es menor que cero o mayor que 60, deberá mostrar el siguiente mensaje: 
    **Error en los datos**
Si los datos son correctos se deberá calcular de la siguiente manera: 
 * El costo de la primera hora o fracción de hora es de 10 pesos. 
 * A partir de la segunda hora, se cobra cada 15 minutos 2 pesos
## Ejemplos  

Ejemplo 1    

```plaintext
Horas: -5
Error en los datos
```

Ejemplo 2

```plaintext
Horas: 0
Minutos: 23
Total a pagar: 10
```

Ejemplo 3

```plaintext
Horas: 1
Minutos: 80
Error en los datos
```

Ejemplo 4
```plaintext
Horas: 1
Minutos: 35
Total a pagar: 16
```

Ejemplo 5
```plaintext
Horas: 2
Minutos: 12
Total a pagar: 20
```



**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.
