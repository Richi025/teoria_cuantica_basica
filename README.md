# Teoria Cuántica Básica. observables y Medidas.

El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes

## Operaciones(Simulaciones) Soportadas en la libreria

La biblioteca incluye las siguientes funciones para operar con vectores y matrices complejas. Los números complejos dentro de cada vector o matriz se representan utilizando el tipo "complex" de la biblioteca numpy de Python, donde la primera parte corresponde a la parte real y la segunda parte a la parte imaginaria.

1. **probabilidad de encontrarlo en una posición en particular:** `probSisLinea(vector, pos)`
2. **probabilidad de transitar del primer vector al segundo:** `probabilityOfTransit(vector_1, vector_2)`
3. **Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación**`amplitudeOfTransit(vector_1, vector_2)`
<<<<<<< HEAD
4. **el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media  del observable en el estado dado** `mediaObservableKet(matrixObservable, Ket_vector)`
5. **el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la varianza del observable en el estado dado** `variationObservableKet(matrix,vector)`
6. **El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.** `val_propios_and_probability_of_transition_to_vec_propio(vec_state, matrix_observable)`
7. **Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.** `sistem_dinamic(vec_state, matrix_s)`

## Discusión de los ejercicios
1. 4.5.2
![WhatsApp Image 2023-10-23 at 4 22 11 PM](https://github.com/Richi025/teoria_cuantica_basica/assets/138072260/07ed5ea3-8e0f-45e9-88f9-e6c251e1117b)

2. 4.5.3
![WhatsApp Image 2023-10-23 at 4 22 11 PM](https://github.com/Richi025/teoria_cuantica_basica/assets/138072260/7bb209c4-b0f4-4c8a-a253-0bfcf3f50fa5)


## Uso
Instrucciones:
1. Clona este repositorio en tu máquina local.
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones de para realizar simulaciones de experimentos cuánticos.

## Ejemplo de Uso

```python
import basic_quantum_theory as tl

# probabilidad de transitar del primer vector al segundo
vector_1 = [complex(0, 1), complex(-1, 0)]
vector_2 = [complex(1, 0), complex(0, -1)]

result = tl.probabilityOfTransit(vector_1, vector_2)
print("Simulacion :", result)
```

## Requisitos

Antes de comenzar con la ejecución de los contenidos de este repositorio, es esencial verificar que Python esté instalado en su computadora, ya que este es el lenguaje en el que se ha desarrollado este repositorio.

1. Dirijase a la página https://www.python.org/downloads/
2. De click en la opción de descarga o al siguiente enlace:
- [PyCharm 3.11](https://www.jetbrains.com/pycharm/)
3. Ejecute el programa que se descarga automáticamente.
4. Complete la instalacion.

## Versión

**Versión Final**

## Autor
**Jose Ricardo Vasquez Vega**
