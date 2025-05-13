def busca_distancia(grafo, inicio):
    n = len(grafo)
    visitado = [False] * n
    distancia = [0] * n
    fila = [inicio]

    visitado[inicio] = True

    while fila:
        atual = fila.pop(0)
        for vizinho in range(n):
            if grafo[atual][vizinho] == 1 and not visitado[vizinho]:
                visitado[vizinho] = True
                distancia[vizinho] = distancia[atual] + 1
                fila.append(vizinho)

    return distancia

def maior_distancia(grafo):
    n = len(grafo)
    maior = 0

    for i in range(n):
        distancias = busca_distancia(grafo, i)
        maior_do_no = max(distancias)
        if maior_do_no > maior:
            maior = maior_do_no

    return maior

print(''' 
Função busca_distancia(grafo, inicio)
    n ← tamanho de grafo
    visitado ← vetor de n posições multiplicado False
    distancia ← vetor de n posições com 0
    fila ← fila com o elemento inicio

    visitado[inicio] ← Verdadeiro

    Enquanto fila não estiver vazia faça
        atual ← remover o primeiro elemento de fila

        Para vizinho de 0 até n - 1 faça
            Se grafo[atual][vizinho] = 1 e visitado[vizinho] = Falso então
                visitado[vizinho] ← Verdadeiro
                distancia[vizinho] ← distancia[atual] + 1
                adicionar vizinho ao final da fila
            Fim Se
        Fim Para
    Fim Enquanto

    Retornar distancia
Fim Função
''')