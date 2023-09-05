import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_erros = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        numero_erros += 1
        continue
    if len(letra_digitada) < 1:
        numero_erros += 1
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    else:
        numero_erros += 1

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ', palavra_formada)
    chute = input('Quer dar um chute? [s/n]').strip().lower()
    if chute == 's':
        palavra_chutada = input('Dê seu chute: ').lower().strip()
    else:
        continue
    if palavra_formada == palavra_secreta or palavra_chutada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Erros: ', numero_erros)
        numero_erros = 0
        palavra_formada = ''
    print('Fim do jogo.')