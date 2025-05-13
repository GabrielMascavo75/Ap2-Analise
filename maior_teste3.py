from func__maior_distancia import maior_distancia

grafo_matriz3 = [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1, 0]]
print("Maior distância no grafo 3:", maior_distancia(grafo_matriz3))