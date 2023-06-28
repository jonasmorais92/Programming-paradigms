#FUNÇÕES RETORNANDO VALORES MÍNIMO E MÁXIMO

def encontrar_menor(lista):
    minimo = lista[0]
    for elem in lista:
        if (elem < minimo):
            minimo = elem
    return minimo

lista_teste = [8,16,14,88,56,20,1,13,94]
menor = encontrar_menor(lista_teste)
print(f"O menor valor é {menor}.")

def encontrar_maior(lista):
    maximo = lista[0]
    for elem in lista:
        if (elem > maximo):
            maximo = elem
    return maximo

lista_teste = [8,16,14,88,56,20,1,13,94]
maior = encontrar_maior(lista_teste)
print(f"O maior valor é {maior}.")