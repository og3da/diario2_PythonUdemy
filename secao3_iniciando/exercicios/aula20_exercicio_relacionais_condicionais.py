primeiro_valor = input('digite o primeiro valor: ')
segundo_valor = input('digite o segundo valor: ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

try:
    print()
    if primeiro_valor > segundo_valor:
        print(f'o primeiro_valor={primeiro_valor} é maior que o segundo_valor={segundo_valor}')
    elif segundo_valor > primeiro_valor:
        print(f'o segundo_valor={segundo_valor} é maior que o primeiro_valor={primeiro_valor}')
    elif primeiro_valor == segundo_valor:
        print('valores iguais')
    else:
        print('digite um valor válido')
except:
    print('ERRO - digite um valor válido')