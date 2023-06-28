#SEQUENCIA DE FIBONACCI (1,1,2,3,5,8...  Começa com 1,1 e a partir da posição 3 da sequencia é somado os dois ultimos valores pra indicar o proximo. exemolo, 2,3, o prx é o 5)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

resultado = fibo(5) #RETORNA O NUMERO QUE SE ALOCA NA POSIÇÃO 5 DA SEQUENCIA DE FIBONACCI
print(resultado)
print(help(fibo))