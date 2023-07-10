teste_num = input('digite um numero inteiro: ')

if teste_num.isdigit():
    num = input('digite um numero inteiro: ')
    num = int(num)
    if (num % 2 == 0):
        print('numero par')
    elif (num % 2 != 0):
        print('numero impar')
else:
    print('errado n e digito')