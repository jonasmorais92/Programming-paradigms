"""#SOMANDO NUMERO PARES     USANDO LAÇO FOR E CONDICIONAIS

lista = [10,15,20,25,30,35,40]
soma = 0

n = len(lista)

for i in range(n):
    if(lista[i]%2==0):
        soma = soma + lista[i]
print(f'O valor da soma de todos os números pares é de: {soma}')"""



#BOAS PRATICAS, TROCANDO [i] POR [num] NO LAÇO FOR

lista = [10,15,20,25,30,35,40]
soma = 0

for num in lista:
    if(num%2==0):
        soma=soma+num
print(f'O valor da soma de todos os números pares é de: {soma}')