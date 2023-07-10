"""
FAÇA UMA CALCULADORA QUE PEDE 2 NUMEROS AO USUARIO
E PERGUNTE A OPERAÇÃO BASICA AFAZER (+, -, /, *)
"""
try:
    while True:
        print()
        print('-' * 10)
        n1 = input('digite um número: ')
        n2 = input('digite um número: ')
        n1 = float(n1)
        n2 = float(n2)
        print('-' * 10)
        operacao = input('escolha uma operação das opções: \n + SOMA \n - SUBTRAÇÃO \n * MULTIPLICAÇÃO \n / DIVISÃO \n\n opção: ')
        print('-' * 10)
        
        if operacao == '+':
            resultado = n1 + n2
        elif operacao == '-':
            resultado = n1 - n2
        elif operacao == '*':
            resultado = n1 * n2
        elif operacao == '/':
            resultado = n1 / n2
        else:
            print('digite uma operação válida')
            
        print(f'resultado= {resultado}')
        print()
        print('-' * 10)
        sair= input('deseja sair? \n S=SIM \n N=NAO \n opção: ')
        if sair.lower() == 's':
            print('-' * 10)
            print('encerrando')
            break
        else:
            continue
except:
    print('erro inesperado')
    