# https://www.programiz.com/online-compiler/08MgU11ZHDnyK
import math
import time
import tracemalloc

tracemalloc.start()

tiempo_inicio = time.time()
for n in range(1, 12):
    cont = 0    
    
    for i in range(1, n + 1):
        if n % i == 0:
            cont += 1

    if cont == 2:
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")


tiempo_fin = time.time()

memoria_actual, memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print("\n--- Resultados de rendimiento ---")
print(f"Tiempo de ejecución: {tiempo_fin - tiempo_inicio:.6f} segs")
print(f"Memoria usada: {memoria_actual / 1024:.2f} KB")
print(f"Pico de memoria: {memoria_pico / 1024:.2f} KB")
