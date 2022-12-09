import pandas as pd
import numpy as np
import random

# Defino los valores de los intereses.

# Valor de inversion
valorInversion = 50000

# CDTs
r1 = 0.13
# Bienes raices
r2 = 0.04
# https://a2censo.com/campaignNew/836
r3 = [-0.5, 0.16]
# cultivos
r4 = [-1, 0.18]
# criptomonedad https://preahorro.com/invertir/riesgos-de-invertir-en-bitcoin/
r5 = [-0.70, 0.70]

def individuo(valorInversion):
    listGenes = []
    gen = 0
    for i in range(0,4):
        valorInversion = valorInversion - gen
        gen = random.randint(0, valorInversion)
        listGenes.append(gen)
    valorInversion = valorInversion - gen
    listGenes.append(valorInversion)
    return listGenes

# Construyo la poblacion
poblacion = []
for i in range(0,6):
    poblacion.append(individuo(valorInversion))
print(poblacion)

print(len(poblacion))

#print(round(random.uniform(-0.5,0.16),2))

