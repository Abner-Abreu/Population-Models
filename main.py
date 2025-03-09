import matplotlib.pyplot as plt
import numpy as np

def verhulst_model(r, x0, n_terms):
    x = [x0]
    for i in range(n_terms - 1):
        x.append(r * x[-1] * (1 - x[-1]))
    return x

# Parámetros
r = 3
x0 = 0.3
iteraciones = 40 # Reducido para mejor visualización

# Generar datos
x = verhulst_model(r, x0, iteraciones)

plt.figure(figsize=(10, 6))
plt.plot(x, 'bo', markersize=8, linestyle='none', label=f'r = {r}')

# Configurar eje x para mostrar solo enteros
plt.xlabel('Iteración (n)', fontsize=12)
plt.ylabel('Población Normalizada', fontsize=12)
plt.title('Modelo de Verhulst - Iteraciones', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()