dic = {
    '1':lambda x,y: x + y,
    '2':lambda x,y: x - y,
    '3':lambda x,y: x * y,
    '4':lambda x,y: x / y,
    '5':lambda x,y: exit()
}

while True:
    try: #bloco com potencial travamento
        n1 = float(input('N1: '))
        n2 = float(input('N2: '))

        op = input(f'Digite a opção desejada \n' \
                    f'1 - Soma \n' \
                    f'2 - Subtração \n' \
                    f'3 - Multiplicação \n' \
                    f'4 - Divisão \n' \
                    f'5 - Sair \n')
        res = dic[op](n1,n2)
    except ZeroDivisionError:
        print(f'Não dividiras por zero')
    except KeyError:
        print(f'Digite uma opção válida')
    except ValueError:
        print(f'Digite apenas números')
    except Exception as err:
        print(f'Erro desconhecido', err)
    else:
        #proxima instrução caso for bem sucedido    
        print(res)
    finally:
        print(f'Fim da execução!')

