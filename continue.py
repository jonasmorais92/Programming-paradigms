#A OPCAO CONTINUE FAZ COM QUE O CODIGO PULE APENAS A ITERAÇÃO CORRENTE, E NÃO O LAÇO TODO COMO O (BREAK).

for num in range(1,11):
    if num == 5:
        continue
    else:
        print(num)
print('O numero 5 foi pulado, pois caiu na condição do if.')