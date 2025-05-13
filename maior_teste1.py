from func__maior_distancia import maior_distancia

grafo_matriz1 = [[0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1],
                 [1, 1, 0, 1, 1, 0],
                 [0, 1, 1, 0, 1, 1],
                 [0, 0, 1, 1, 0, 1],
                 [0, 1, 0, 1, 1, 0]]
print("Maior distância no grafo 1:", maior_distancia(grafo_matriz1))