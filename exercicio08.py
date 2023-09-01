nome = 'Pilar Leminski Veiga'

tamanho_nome = len(nome)
i = 0
nova_string = '*'

while i < tamanho_nome:
    nova_string += nome[i] + '*'
    i += 1

print(nova_string)