frase = input("Digite uma frase: ")

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    i += 1
    if letra_atual == ' ':
        continue

    qtd_atual = frase.count(letra_atual)
    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    

print(f'A letra que apareceu mais vezes foi {letra_apareceu_mais_vezes}, que apareceu {qtd_apareceu_mais_vezes}x')