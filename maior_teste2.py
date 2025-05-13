from func__maior_distancia import maior_distancia

grafo_matriz2 = [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1],
                 [0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 1, 0]]
print("Maior distância no grafo 2:", maior_distancia(grafo_matriz2))