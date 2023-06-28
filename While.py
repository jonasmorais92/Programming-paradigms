while True:
    print('Primeiro laço')
    opcao1 = input('Escreva sim para sair do laço, ou c para ir pro outro laço')
    if opcao1 == 'sim':
        break
    else:
        while True:
            print('Segundo laço')
            opcao2 = input('Voce esta no segundo laço, deseja sair?')
            if opcao2 == 'sim':
                break
print('Você esta fora dos laços')