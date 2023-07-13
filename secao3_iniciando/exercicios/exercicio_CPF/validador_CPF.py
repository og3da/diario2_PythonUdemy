# ---> CALCULANDO 1º DIGITO
# variáveis para manipular CPF
cpf = input('digite seu cpf: ')
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
print('-' * 10)
if digito_1 == int(cpf[-2]) and digito_2 == int(cpf[-1]):
    print(f'CPF {cpf} válido!')
else:
    print(f'CPF {cpf} inválido!')
print('-' * 10)