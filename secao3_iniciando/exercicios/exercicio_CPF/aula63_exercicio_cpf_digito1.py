"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# variáveis para manipular CPF
cpf = '746.824.890-70'
cpf_formatado = cpf[0:11].split('.')
cpf_unificado = ''
cpf_lista_digitos = []
cpf_lista_digitos_multiplicados = []

# variáveis para realizar cálculos
multiplicador = 10
soma = 0

# na lista cpf_formatado que contem 3 indices de 3 digitos cada, estou unificando na lista cpf_unificado
for i in cpf_formatado:
    cpf_unificado += i

# separando cada digito em cpf_lista_digitos para realizar a multiplicação
for digito in cpf_unificado:
    cpf_lista_digitos += digito

# iterando em cada valor da lista cpf_lista_digitos e realizando a multiplicação, valores acrescentados na lista cpf_lista_digitos_multiplicados
for digito in cpf_lista_digitos:
    digito = int(digito)
    digito *= multiplicador
    cpf_lista_digitos_multiplicados.append(digito)
    multiplicador -= 1

# somando os valores da lista cpf_lista_digitos_multiplicados
for valor in cpf_lista_digitos_multiplicados:
    soma += valor

# Multiplicar o resultado anterior por 10
soma *= 10

# Obter o resto da divisão da conta anterior por 11
resto_soma = soma % 11

# definindo digito usando operações ternarias
digito = 0 if resto_soma > 9 else resto_soma

# RETORNO CONSOLE
print('-' * 10)
print(f'o primeiro dígito é = {digito}')