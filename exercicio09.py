while True:
    while True:
        numero_1 = input('n1: ')
        try:
            numero_1_float = float(numero_1)
            break
        except:
            print('Por favor, digite um número')
    while True:
        numero_2 = input('n2: ')
        try:
            numero_2_float = float(numero_2)
            break
        except:
            print('Por favor, digite um número')
    while True:
        operador = input('Escolha a operação [+ - * /]: ')
        operacao = '+-*/'
        if operador not in operacao:
            print('Operação inválida.')
        if len(operador) > 1:
            print('Digite apenas um operador: ')
            continue
        else:
            break
    if operador == '+':
        res = numero_1_float + numero_2_float
    elif operador == '-':
        res = numero_1_float - numero_2_float
    elif operador == '*':
        res = numero_1_float * numero_2_float
    elif operador == '/':
        res = numero_1_float / numero_2_float
    print(f'{numero_1_float} {operador} {numero_2_float} = {res}')
    sair = input('Deseja sair? [s/n] ')
    if sair in 'sS':
        break
