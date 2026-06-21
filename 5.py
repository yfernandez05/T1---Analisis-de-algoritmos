grafo = {
    "Lima":{"Arequipa":10,"Trujillo":5},
    "Arequipa":{"Lima":10,"Cusco":4},
    "Cusco":{"Arequipa":4,"Piura":8},
    "Trujillo":{"Lima":5,"Chiclayo":3},
    "Piura":{"Cusco":8,"Chiclayo":6},
    "Chiclayo":{"Trujillo":3,"Piura":6}
}
import heapq

def prim(grafo, inicio):

    visitados = set([inicio])
    aristas = []

    for vecino, peso in grafo[inicio].items():
        heapq.heappush(aristas, (peso, inicio, vecino))

    mst = []

    while aristas:
        peso, origen, destino = heapq.heappop(aristas)

        if destino not in visitados:
            visitados.add(destino)
            mst.append((origen, destino, peso))

            for vecino, costo in grafo[destino].items():
                if vecino not in visitados:
                    heapq.heappush(aristas,
                                   (costo, destino, vecino))

    return mst

print(prim(grafo, "Lima"))