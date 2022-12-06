import numpy as np
import pandas as pd
import random
import math

token "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"

# Defino los individuos
numIndividuos = 3
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

# Creo la funcion de ventana de la población y el fitness de cada individuo

def poblacion(numIndividuos, numGenes, rango):
    poblacion = []
    for i in range(0, numIndividuos):
        s= []
        for j in range(0, (numGenes)):
            s.append(random.uniform(-rango,rango)) 
            #print(s)
        evaluacion = funcion_evaluacion(s, contEvaluacion)
        fitness = evaluacion[0]
        s.append(fitness)
        poblacion.append(s)
    return poblacion

# Organizo la poblacion

poblacioninicial = poblacion(numIndividuos, numGenes, rango)
print(poblacioninicial)

def poblacion_organizada(poblacion, numIndividuos, numGenes):
    vectorFitness = []
    for i in range(0, numIndividuos):
        vectorFitness.append(poblacion[i][numGenes])
        #print(vectorFitness)
    vectorFitness.sort(reverse=True)
    for z in range(0,len(vectorFitness)):
        for j in range(0, numIndividuos):
            if poblacion[j] == vectorFitness[z]:
                
    return vectorFitness

result = poblacion_organizada(poblacioninicial, numIndividuos, numGenes )

print(result)
        


