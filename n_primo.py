#NUMERO PRIMO

def ehprimo(n):
    if(n<2):
        return False
    i = n//2
    while (i>1):
        if(n%i==0):
            return False
        i=i-1
    return True

def imprimir_msg(numero, resultado):
        mensagem = f'O numero {numero} NÃO é primo.'
        if (resultado):
             mensagem = f'O numéro {numero} é primo.'
        return mensagem

numero = eval(input('Digite um número: '))
resultado = ehprimo(numero)
msg = imprimir_msg(numero,resultado)
print(msg)
