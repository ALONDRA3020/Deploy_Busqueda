from django.shortcuts import render
from .busquedas import *
from .arbol import Nodo


def convertir_lista(texto):

    return [int(x) for x in texto.split(',')]


def index(request):

    resultado = None
    error = None

    if request.method == 'POST':

        try:

            algoritmo = request.POST['algoritmo']

            estado_inicial = convertir_lista(
                request.POST['estado_inicial']
            )

            solucion = convertir_lista(
                request.POST['estado_final']
            )

            nodo = None

            if algoritmo == 'bfs':

                nodo = buscar_bfs(
                    estado_inicial,
                    solucion
                )

            elif algoritmo == 'dfs':

                nodo = buscar_dfs(
                    estado_inicial,
                    solucion
                )

            elif algoritmo == 'recursiva':

                visitados = []

                nodo_inicial = Nodo(
                    estado_inicial
                )

                nodo = buscar_recursiva(
                    nodo_inicial,
                    solucion,
                    visitados
                )

            if nodo:

                resultado = []

                while nodo.get_padre() != None:

                    resultado.append(
                        nodo.get_datos()
                    )

                    nodo = nodo.get_padre()

                resultado.append(
                    estado_inicial
                )

                resultado.reverse()

            else:

                error = "No se encontró solución"

        except:

            error = "Formato inválido"

    return render(
        request,
        'algoritmos/index.html',
        {
            'resultado': resultado,
            'error': error,

            'estado_inicial': request.POST.get(
                'estado_inicial',
                ''
            ),

            'estado_final': request.POST.get(
                'estado_final',
                ''
            ),

            'algoritmo': request.POST.get(
                'algoritmo',
                ''
            )
        }
    )