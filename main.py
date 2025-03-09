import matplotlib.pyplot as plt
import src.models.verhulst_model as verhulst
# Parámetros

iteraciones = 40 # Reducido para mejor visualización

# Generar datos
x = verhulst.logistic_model(0.3,1000,100,50)

plt.figure(figsize=(10, 6))
plt.plot(x, 'bo', markersize=8, linestyle='none')

plt.xlabel('Iteración (n)', fontsize=12)
plt.ylabel('Población', fontsize=12)
plt.title('Modelo de Verhulst', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()