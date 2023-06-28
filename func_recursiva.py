#FUNÇÃO COM RECURSIVIDADE (FUNÇAO INVOCA ELA MESMA)

def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)
    
resultado = fatorial(4)
print(resultado)