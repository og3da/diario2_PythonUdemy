"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# ---> CALCULANDO 1º DIGITO
# variáveis para manipular CPF
cpf = '746.824.890-70'
cpf_formatado = cpf[0:11].split('.')
cpf_unificado = ''

# variáveis para realizar cálculos
multiplicador = 10
resultado = 0

# concatenando os 9 digitos na str cpf_unificado
for i in cpf_formatado:
    cpf_unificado += i

# iterando em cada valor da str cpf_unificado e realizando a multiplicação, valores final na var resultado
for digito in cpf_unificado:
    resultado += int(digito) * multiplicador
    multiplicador -= 1

# Multiplicar o resultado anterior por 10 mod 11
resultado = (resultado * 10) % 11

# definindo digito_1 usando operações ternarias
digito_1 = 0 if resultado > 9 else resultado

# RETORNO CONSOLE
print('-' * 10)
print(f'o primeiro dígito é = {digito_1}')



# ---> CALCULANDO 2º DIGITO
cpf_unificado += str(digito_1)

# variáveis para realizar cálculos
multiplicador = 11
resultado_2 = 0

# iterando em cada valor da str cpf_unificado e realizando a multiplicação, valores final na var resultado_2
for digito in cpf_unificado:
    resultado_2 += int(digito) * multiplicador
    multiplicador -= 1

# Multiplicar o resultado_2 anterior por 10 mod 11
resultado_2 = (resultado_2 * 10) % 11

# definindo digito_2 usando operações ternarias
digito_2 = 0 if resultado_2 > 9 else resultado_2

# RETORNO CONSOLE
print(f'o segundo dígito é = {digito_2}')
print('-' * 10)