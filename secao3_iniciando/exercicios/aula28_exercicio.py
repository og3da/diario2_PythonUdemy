"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
nome_invertido = nome[::-1]
contem_espaco = 'seu nome NÃO contém espaços'

if nome == '' or idade == '':
    print('Desculpe, você deixou campos vazios')

if ' ' in nome:
    contem_espaco='seu nome contém espaços'

print()
if nome and idade:
    print(f'Seu nome é {nome}\n Seu nome invertido é {nome_invertido}\n {contem_espaco}\n Seu nome tem {len(nome)} letras\n'
          f'A primeira letra do seu nome é= {nome[0]}\n A última letra do seu nome é= {nome[-1]}'
          )