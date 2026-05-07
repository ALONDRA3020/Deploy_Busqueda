from .arbol import Nodo

# BFS
def buscar_bfs(estado_inicial, solucion):

    visitados = []
    frontera = []

    nodo_inicial = Nodo(estado_inicial)
    frontera.append(nodo_inicial)

    while frontera:

        nodo = frontera.pop(0)
        visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo

        dato = nodo.get_datos()

        hijos = []

        hijos_datos = [
            [dato[1], dato[0], dato[2], dato[3]],
            [dato[0], dato[2], dato[1], dato[3]],
            [dato[0], dato[1], dato[3], dato[2]]
        ]

        for h in hijos_datos:
            hijo = Nodo(h)

            if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                hijo.set_padre(nodo)
                frontera.append(hijo)

                hijos.append(hijo)

        nodo.set_hijos(hijos)

    return None


# DFS
def buscar_dfs(estado_inicial, solucion):

    visitados = []
    frontera = []

    nodo_inicial = Nodo(estado_inicial)
    frontera.append(nodo_inicial)

    while frontera:

        nodo = frontera.pop()
        visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo

        dato = nodo.get_datos()

        hijos_datos = [
            [dato[1], dato[0], dato[2], dato[3]],
            [dato[0], dato[2], dato[1], dato[3]],
            [dato[0], dato[1], dato[3], dato[2]]
        ]

        hijos = []

        for h in hijos_datos:

            hijo = Nodo(h)

            if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                hijo.set_padre(nodo)
                frontera.append(hijo)
                hijos.append(hijo)

        nodo.set_hijos(hijos)

    return None


# Recursiva
def buscar_recursiva(nodo, solucion, visitados):

    visitados.append(nodo.get_datos())

    if nodo.get_datos() == solucion:
        return nodo

    dato = nodo.get_datos()

    hijos_datos = [
        [dato[1], dato[0], dato[2], dato[3]],
        [dato[0], dato[2], dato[1], dato[3]],
        [dato[0], dato[1], dato[3], dato[2]]
    ]

    hijos = []

    for h in hijos_datos:

        hijo = Nodo(h)
        hijos.append(hijo)

    nodo.set_hijos(hijos)

    for hijo in nodo.get_hijos():

        if hijo.get_datos() not in visitados:

            hijo.set_padre(nodo)

            sol = buscar_recursiva(hijo, solucion, visitados)

            if sol:
                return sol

    return None