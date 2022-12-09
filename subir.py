#  Cruze entre hijos mediante Clusters
# ===================================================================================
def cruzeHijosClusters(Padre1,Padre2,Nclusters):
    listDimCluster = list(range(1,Nclusters))
    clusterChange = np.random.choice(listDimCluster, 1)
    #print("Cluster a Cambiar: ",clusterChange)
    # Encontramos los indices donde sean iguales cl cluster Seleccionado
    IndexP1 = [indice for indice, dato in enumerate(Padre1) if dato == clusterChange[0]]
    IndexP2 = [indice for indice, dato in enumerate(Padre2) if dato == clusterChange[0]]
    
    # Realizo el intercabio de cluster  - Para Formar los Hijos
    # H1: 1 madre | 2 padre
    for i in range(len(IndexP1)):
        Padre2[IndexP1[i]] = clusterChange[0]

    # H2 #2 madre | 1 padre
    for i in range(len(IndexP2)):
        Padre1[IndexP2[i]] = clusterChange[0]

    c1 = Padre1
    c2 = Padre2
    
    #print("Cruze 1: ",c1)
    #print("Cruze 2: ",c2)
    return c1,c2


# Funcion para remplazar la nueva Poblacion  - Operador del peor
# ==============================================================================
def RemplazoDelPeor(fitP,fitNP,Poblacion,NuevaPoblacion):
    # Agrupanos en una sola lista el fitness de ambas poblaciones
    fitT = fitP + fitNP
    # Agrupamos en una sola lista las poblaciones
    PT = Poblacion + NuevaPoblacion
    # Se convierte la lista de Fitnes Total  a df
    df =  pd.DataFrame(fitT,columns=["Fitnes"])
    # Obtengo los N mejores individuos de acuerdo al tamaño de la población
    df = df.sort_values('Fitnes',ascending=False)[0:len(fitP)]
    # Lista de los mejores valores de Aptitud
    Nfit = list(df.Fitnes)
    # Lista de los indices de la Poblacioón
    indexNuevaPoblacion = list(df.index)
    # Ubicamos los Individuos de la Nueva Población

    NP = []
    for i in range(len(indexNuevaPoblacion)):
        NP.append(PT[indexNuevaPoblacion[i]])
    
    # Retorna la lista de la nueva Poblacion y los respectivos Fitnes
    return NP, Nfit
