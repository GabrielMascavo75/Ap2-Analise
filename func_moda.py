def moda(lista):
    elementos = []
    contagens = []

    for elemento in lista:
        achou = False
        for i in range(len(elementos)):
            if elementos[i] == elemento:
                contagens[i] += 1
                achou = True
                break
        if not achou:
            elementos.append(elemento)
            contagens.append(1)

    maior_contagem = contagens[0]
    indice_moda = 0
    for i in range(1, len(contagens)):
        if contagens[i] > maior_contagem:
            maior_contagem = contagens[i]
            indice_moda = i

    return elementos[indice_moda]


print('''
Função moda(lista)
    elementos ← lista vazia
    contagens ← lista vazia

    Para cada elemento na lista faça
        achou ← FALSO

        Para i de 0 até tamanho(elementos) - 1 faça
            Se elementos[i] = elemento então
                contagens[i] ← contagens[i] + 1
                achou ← Verdadeiro
                Pare
            Se não for achou
                adicione elementos em (elemento)
                adicione contagens em (1)
        maior_contagem ← contagens [i]
        indice

        Se achou = Falso então
            Adicione elemento em elementos
            Adicione 1 em contagens
        Fim Se
    Fim Para

    maior_contagem ← contagens[0]
    indice_moda ← 0

    Para i de 1 até tamanho(contagens) - 1 faça
        Se contagens[i] > maior_contagem então
            maior_contagem ← contagens[i]
            indice_moda ← i
        Fim Se
    Fim Para

    Retorne elementos[indice_moda]
Fim Função

''')