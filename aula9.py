nota = eval(input("Nota do aluno:"))
if(nota>=7.0):
    situacao = 'APROVADO'
elif(nota>=5):
    situacao = ' EM 9RECUPERAÇÃO'
else:
    situacao = 'REPROVADO'

print(f'O estudante está: {situacao}')