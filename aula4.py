nome = 'Jonas da Silva Morais'

print(nome)
print('valor variavel nome = {}'.format(nome))  #algumas formas de print
print(f'valor variavel nome = {nome}')

#############################################

#atribuição multipla

a, b = 1, 2
print('Antes da troca')
print(f'O valor das variaveis a = {a} e b = {b}')

#primeira troca

aux = a
a = b
b = aux

print(f'O valor das variaveis a = {a} e b = {b}')

#segunda troca

a, b = b, a

print(f'O valor das variaveis a = {a} e b = {b}')

################################################

#OPERADORES COMPOSTOS

x = 10
print(f"o valor de x = {x}")
x+=2
print(f"o valor de x = {x}")
x-=2
print(f"o valor de x = {x}")
x*=2
print(f"o valor de x = {x}")
x/=2
print(f"o valor de x = {x}")
x%=2
print(f"o valor de x = {x}")