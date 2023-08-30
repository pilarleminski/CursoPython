nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[len(nome)::-1]

if len(nome) and len(idade):
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome contém {len(nome)} letras')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')
