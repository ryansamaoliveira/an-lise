import pandas as pd
import numpy as np

dados = np.array([10, 25, 56, 8, 17, 12, 85, 49, 72, 1])

q1 = np.percentile(dados, 25) 
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75)

print(f"Primeiro Quartil (mais rapido): {q1}")
print(f"Segundo Quartil (mediana/padrão): {q2}")
print(f"Terceiro Quartil (devagar): {q3}")

media = np.mean(dados)

deltaMediaMediana = media - q2

print(f'Média: {media}')
print(f'Diferença entre média e mediana: {deltaMediaMediana}')