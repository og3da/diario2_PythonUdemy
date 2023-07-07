"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    num = input('digite um numero inteiro: ')
    num = int(num)
    if (num % 2 == 0):
        print('numero par')
    elif (num % 2 != 0):
        print('numero impar')
except ValueError:
    print('não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = input('digite a hora: ')
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('bom dia')
    elif hora >= 12 and hora <= 17:
        print('boa tarde')
    elif hora >= 18 and hora <= 23:
        print('boa noite')
except ValueError:
    print('não é um número inteiro')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('digite seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é grande')
else:
    print('nao sei oq dizer')
    