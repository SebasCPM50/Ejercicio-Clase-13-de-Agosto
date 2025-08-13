# Ejercicio-Clase-13-de-Agosto
Ejercicio Comparación Números Primos
# time
import time: Para poder usar el cronómetro en Python

tiempo_inicio = time.time(): Guarda la hora exacta en la que empieza el programa

tiempo_fin = time.time(): Guarda la hora exacta en la que termina

tiempo_fin - tiempo_inicio: Calcula la diferencia entre el incio y el fin para saber cuánto duró

# tracemalloc
import tracemalloc: Para poder medir memoria en Python

tracemalloc.start(): Empieza a medir la memoria desde ese punto del programa

tracemalloc.get_traced_memory(): Devuelve dos datos: la memoria que está usando en ese momento y la memoria máxima (el tope) que se usó

tracemalloc.stop(): Detiene la medición de memoria
