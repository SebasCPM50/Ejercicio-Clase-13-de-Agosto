# https://www.programiz.com/online-compiler/9tLfmUht2Mns7
import math
import time
import tracemalloc 

tracemalloc.start()

tiempo_inicio = time.time()

for n in range(1, 12):
    if n < 2:
        print(f"{n} no es primo")
        continue
    
    es_primo = True
    limite = int(math.sqrt(n)) + 1

    for i in range(2, limite):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")

tiempo_fin = time.time()

memoria_actual, memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print("\nResultados de rendimiento: ")
print(f"Tiempo de ejecución: {tiempo_fin - tiempo_inicio:.6f} segundos")
print(f"Memoria usada: {memoria_actual / 1024:.2f} KB")
print(f"Pico de memoria: {memoria_pico / 1024:.2f} KB")
