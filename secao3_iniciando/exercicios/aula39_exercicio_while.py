"""
Iterando strings com while
"""
#      

nome = 'Luiz Otávio'  # Iteráveis
nome_str = ''
indice = 0

while indice < len(nome):
    nome_str += nome[indice] + '*'
    indice += 1
print(nome_str)