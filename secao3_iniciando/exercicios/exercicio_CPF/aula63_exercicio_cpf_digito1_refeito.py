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

# variáveis para realizar cálculos
multiplicador = 10
resultado = 0

# concatenando os 9 digitos na str cpf_unificado
for i in cpf_formatado:
    cpf_unificado += i

# iterando em cada valor da str cpf_unificado e realizando a multiplicação, valores final na var resultado
for digito_1 in cpf_unificado:
    resultado += int(digito_1) * multiplicador
    multiplicador -= 1

# Multiplicar o resultado anterior por 10 mod 11
resultado = (resultado * 10) % 11

# definindo digito_1 usando operações ternarias
digito_1 = 0 if resultado > 9 else resultado

# RETORNO CONSOLE
print('-' * 10)
print(f'o primeiro dígito é = {digito_1}')