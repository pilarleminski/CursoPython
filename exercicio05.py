numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    par_ou_impar = numero % 2
    if par_ou_impar == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')
except:
    print('O valor digitado não é um número inteiro.')

