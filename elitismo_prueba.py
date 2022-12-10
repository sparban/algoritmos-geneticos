import numpy as np
import pandas as pd
import random
import math

token = "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"

## https://www.freecodecamp.org/espanol/news/ordenar-listas-en-python-como-ordenar-por-descendente-o-ascendente/

# Defino los individuos
numIndividuos = 2
numGenes = 2
rango = 600
contEvaluacion = 0
# funcion de evaluacion

def funcion_evaluacion(individuo, contEvaluacion):
    contEvaluacion += 1
    y = 0
    for i in range(len(individuo)):
        y = round((individuo[i]*individuo[i]) + y, 2)
    return (y, contEvaluacion)

# Creo la funcion de ventana de la población y el fitness de cada individuo (n individuos)

def poblacion(numIndividuos, numGenes, rango):
    poblacion = []
    for i in range(0, numIndividuos):
        s= []
        for j in range(0, numGenes):
            s.append(random.uniform(-rango,rango)) 
        evaluacion = funcion_evaluacion(s, contEvaluacion)
        fitness = evaluacion[0]
        s.append(fitness)
        poblacion.append(s)
    return poblacion

poblacioninicial = poblacion(numIndividuos, numGenes, rango)
print(poblacioninicial)

# Organizo los individuos de mayor a menor segun el fitness

poblacionOrganizada = sorted(poblacioninicial, key=lambda fitness: fitness[numGenes], reverse=True)

#------------------------ Cruce de un punto ---------------------------

# Valor aleatorio
C = random.randint(1, numGenes-1)
print(C)

listaPadres = poblacionOrganizada[0:2]
padre1 = poblacionOrganizada[0][0:numGenes]
padre2 = poblacionOrganizada[1][0:numGenes]

print(f" lista de padres: {listaPadres}")
print("padre 1: ", padre1)
print("padre 2: ", padre2)

hijo1 = padre1[0:C]
hijo2 = padre2[0:C]

hijo1.extend(padre2[C:len(padre2)])
hijo2.extend(padre1[C:len(padre1)])

print("Hijo 1:", hijo1)
print("Hijo 2:", hijo2)

