from django.shortcuts import render
from .busquedas import *
from .arbol import Nodo


def convertir_lista(texto):

    return [int(x) for x in texto.split(',')]


def obtener_camino(nodo, estado_inicial):

    resultado = []

    while nodo.get_padre() != None:

        resultado.append(
            nodo.get_datos()
        )

        nodo = nodo.get_padre()

    resultado.append(estado_inicial)

    resultado.reverse()

    return resultado


def index(request):

    bfs_resultado = None
    dfs_resultado = None
    rec_resultado = None

    error = None

    if request.method == 'POST':

        try:

            estado_inicial = convertir_lista(
                request.POST['estado_inicial']
            )

            solucion = convertir_lista(
                request.POST['estado_final']
            )

            # BFS
            nodo_bfs = buscar_bfs(
                estado_inicial,
                solucion
            )

            if nodo_bfs:

                bfs_resultado = obtener_camino(
                    nodo_bfs,
                    estado_inicial
                )

            # DFS
            nodo_dfs = buscar_dfs(
                estado_inicial,
                solucion
            )

            if nodo_dfs:

                dfs_resultado = obtener_camino(
                    nodo_dfs,
                    estado_inicial
                )

            # Recursiva
            visitados = []

            nodo_inicial = Nodo(
                estado_inicial
            )

            nodo_rec = buscar_recursiva(
                nodo_inicial,
                solucion,
                visitados
            )

            if nodo_rec:

                rec_resultado = obtener_camino(
                    nodo_rec,
                    estado_inicial
                )

        except:

            error = "Formato inválido"

    return render(
        request,
        'algoritmos/index.html',
        {
            'bfs_resultado': bfs_resultado,
            'dfs_resultado': dfs_resultado,
            'rec_resultado': rec_resultado,
            'error': error
        }
    )