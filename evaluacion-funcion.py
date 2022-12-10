import pandas as pd
import numpy as np
import random

# Defino los valores de los intereses.

# Valor de inversion
valorInversion = 500

# CDTs
r1 = 0.13
# Bienes raices
r2 = 0.04
# https://a2censo.com/campaignNew/836
r3 = [-0.5, 0.16]
#  GRUPO TELINTEL SA ESP
r4 = [-0.5, 0.18]
# criptomonedad https://preahorro.com/invertir/riesgos-de-invertir-en-bitcoin/
r5 = [-0.1, 0.2]

# tasas de interes

rtotal = [r1,r2,r3,r4,r5]

# Tamaño de la poblacion

poblacionNum = 50

# Numero de genes

numGenes = 5

poblacionOriginal = []

contEvaluacion = 0

fitnesPrimero = 0

# % ganancia

ganancia = 0.01

# defino el individuo que cumpla las caracteristicas (su valores no sumen mas de 50.000)
def funcion_individuo(valorInversion):
    listGenes = []
    gen = 0
    for i in range(0,4):
        valorInversion = valorInversion - gen
        gen = random.randint(0, valorInversion)
        listGenes.append(gen)
    valorInversion = valorInversion - gen
    listGenes.append(valorInversion)
    return listGenes

# -----------------poblacion inicial -------------------

def poblacion_original (poblacionNum):
    for i in range (0,poblacionNum):
        individuo = funcion_individuo(valorInversion)
        poblacionOriginal.append(individuo)
    return poblacionOriginal

#print("poblacion inicial", poblacioninicial)
#---------------------- Funcion de evaluacion------------------------------------

def evaluacion(poblacioninicial,r1,r2,r3,r4,r5, contEvaluacion):
    intereses = []
    for i in range(0, len(poblacioninicial)):
        contEvaluacion += 1
        g1 = poblacioninicial[i][0] + r1*poblacioninicial[i][0]
        g2 = poblacioninicial[i][1] + r2*poblacioninicial[i][1]
        interes1 = round(random.uniform(r3[0],r3[1]),2)
        interes2 = round(random.uniform(r4[0],r4[1]),2)
        interes3 = round(random.uniform(r5[0],r5[1]),2)
        g3 = poblacioninicial[i][2] + interes1*poblacioninicial[i][2]
        g4 = poblacioninicial[i][3] + interes2*poblacioninicial[i][3]
        g5 = poblacioninicial[i][4] + interes3*poblacioninicial[i][4]
        fitnes = g1+g2+g3+g4+g5
        intereses = [interes1, interes2, interes3]
        poblacioninicial[i].append(fitnes)
        poblacioninicial[i].append(intereses)
        
    return(poblacioninicial, contEvaluacion)


#----------------------Operador de selección: elitismo ---------------------------


def seleccion_elitismo (poblacioninicialPlusFitness):
    poblacionOrganizada = sorted(poblacioninicialPlusFitness, key=lambda fitness: fitness[numGenes], reverse=True)
    #print("poblacion organizada", poblacionOrganizada)
    listaPadres = poblacionOrganizada[0:2]
    padre1 = poblacionOrganizada[0][0:numGenes]
    padre2 = poblacionOrganizada[1][0:numGenes]
    #print(padre1)
    #print(padre2)
    #print(f" lista de padres: {listaPadres}")
  
    return padre1, padre2

#--------------------- Operador de seleccion: aleatorio--------------------

def seleccion_aleatorio (poblacioninicialPlusFitness, poblacionNum, numGenes):
    IndexPadre1 = random.randint(0,poblacionNum-1)
    IndexPadre2 = random.randint(0,poblacionNum-1)
    padre1 = poblacioninicialPlusFitness[IndexPadre1][0:numGenes]
    padre2 = poblacioninicialPlusFitness[IndexPadre2][0:numGenes]

    return padre1, padre2

#-----------------------Operador de cruce: un punto ---------------------------

def cruce_un_punto(numGenes, padre1, padre2):
    C = random.randint(1, numGenes-1)
    hijo1 = padre1[0:C]
    hijo2 = padre2[0:C]
    hijo1.extend(padre2[C:len(padre2)])
    hijo2.extend(padre1[C:len(padre1)])
    diferencia1 = valorInversion - sum(hijo1)
    diferencia2 = valorInversion -sum(hijo2)

    valorSuma1 = diferencia1
    valorSuma2 = diferencia2

    index1 = hijo1.index(max(hijo1))
    index2 = hijo2.index(max(hijo2))
    
    hijo1[index1] = hijo1[index1]+valorSuma1
    hijo2[index2] = hijo2[index2]+valorSuma2
  
    return hijo1, hijo2

#------------------ Operacion Mutación: intercambio ------------------------

def mutacion_intercambio(hijo1, hijo2):
    random.shuffle(hijo1)
    random.shuffle(hijo2)
    return hijo1, hijo2

#--------------------- Construyo lista de hijos -------------------------------

def lista_hijos (poblacionNum, poblacioninicialPlusFitness, numGenes): 
    ListaHijos = []

    for i in range(0, int(poblacionNum/2)):

        padres = seleccion_elitismo(poblacioninicialPlusFitness)
        #padres = seleccion_aleatorio(poblacioninicialPlusFitness, poblacionNum, numGenes)
        padre1 = padres[0]
        padre2 = padres[1]

        hijos = cruce_un_punto(numGenes, padre1, padre2)
        hijo1 = hijos[0]
        hijo2 = hijos[1]
        
        hijosMutados = mutacion_intercambio(hijo1, hijo2)
        hijoMutado1 = hijosMutados[0]
        hijoMutado2 = hijosMutados[1]

        # Creo nueva lista de hijos 

        ListaHijos.append(hijoMutado1)
        ListaHijos.append(hijoMutado2)
    return ListaHijos


# ---------------- Genero el vector original ----------------------------
poblacioninicial = poblacion_original(poblacionNum)
poblacioninicialPlusFitnessVector = evaluacion(poblacioninicial,r1,r2,r3,r4,r5, contEvaluacion)
poblacioninicialPlusFitness = poblacioninicialPlusFitnessVector[0]
contEvaluacion = poblacioninicialPlusFitnessVector[1]

while fitnesPrimero <= (valorInversion + ganancia*valorInversion):
    #------------------ Operacion de reemplazo: Del peor ------------------------
    # Evaluo fitness de los hijos
    ListaHijos = lista_hijos(poblacionNum, poblacioninicialPlusFitness, numGenes)
    poblacionHijosPlusFitnessVector = evaluacion(ListaHijos,r1,r2,r3,r4,r5, contEvaluacion)
    poblacionHijosPlusFitness = poblacionHijosPlusFitnessVector[0]
    contEvaluacion = poblacionHijosPlusFitnessVector[1]
    if contEvaluacion >= 5000:
        break
    # ----------------- Concateno lista de hijos y de padres ---------------------
    listaTotal = poblacioninicialPlusFitness + poblacionHijosPlusFitness
    poblacionQ = sorted(listaTotal, key=lambda fitness: fitness[numGenes], reverse=True)
    # Escogo los mejores individuos
    ListaNueva = poblacionQ[0:poblacionNum]
    #print("Lista nueva: ", ListaNueva)
    
    #----------------- Genero los vectores correspondientes (sin los porcentajes) ---------------
    ListaReemplazo = []
    for i in range(0, poblacionNum):
        ListaReemplazo.append(ListaNueva[i][0:numGenes+1])
        
    #----------------- Reemplazo la lista original -------------------------------
    
    poblacioninicialPlusFitness = ListaReemplazo
    
    fitnesPrimero = ListaNueva[4][5]
    #print("Mejor fitness", fitnesPrimero)
    
#print(fitnesPrimero)
print("Top5 inversiones: ", ListaReemplazo[0:5])
#print("Lista nueva", ListaNueva)
