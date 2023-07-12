"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import traceback
import os
import time

lista_compras = []
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-' * 10)
        opcao = input('SELECIONE UMA OPÇÃO\n [i]nserir \n [a]pagar \n [l]istar \n\n opção: ')
        print('-' * 10)
        print('')
        if opcao == 'i':
            item = input('digite o item: ')
            lista_compras.append(item)
            print(f'item {item} adicionado com sucesso')
            time.sleep(4)
            continue
        elif opcao == 'a':
            for indice, item in enumerate(lista_compras):
                print(indice, item)
            print()
            indice = int(input('digite o índice a apagar: '))
            if indice > len(lista_compras):
                print('digite um índice válido!')
                time.sleep(4)
                continue
            else:
                lista_compras.pop(indice)
                print(f'indice {indice} apagado com sucesso')
                time.sleep(4)
                continue
        elif opcao == 'l':
            if len(lista_compras) == 0:
                print('LISTA VAZIA')
                time.sleep(4)
                continue
            else:
                for indice, item in enumerate(lista_compras):
                    print(indice, item)
                time.sleep(4)
                continue
        else:
            print('digite uma opção válida!')
            time.sleep(4)
            continue
    except ValueError:
        print('ERRO --> digite um valor inteiro!')
        time.sleep(4)
        continue
    except:
        traceback. print_exc()
        break
