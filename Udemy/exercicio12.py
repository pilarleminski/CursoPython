lista = ['Maria', 'Helena', 'Luiz']

i = 0
for nome in lista:
    print(i, nome)
    i += 1

# Resolulção do professor

print('=' * 10)

indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])

# Resolução com enumerate
print('=' * 10)

for indice, nome in enumerate(lista):
    print(indice, nome)