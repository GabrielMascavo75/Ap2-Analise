from func_moda import moda

lista2 = [i//10 for i in range(100, -10 , -1)] + [10, 11, 12, 13 ,14, 5, 16, 17,18, 19]
print("Moda teste 2 : ", moda(lista2))

print('''
Importar a função moda do módulo func_moda

Crie lista2:
    Enquanto i for 0, decremente de 1 em 1:
        Adicionar (I dividido por 10, usando divisão inteira) à LISTA2
    Depois, adicionar os seguintes valores à LISTA2:
        10, 11, 12, 13, 14, 5, 16, 17, 18, 19

MODA_RESULTADO ← chamar MODA(LISTA2)

Exibir "Moda teste 2: ", seguido do valor de MODA_RESULTADO
''')