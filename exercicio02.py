# Cálculo IMC

nome = 'Pilar'.upper()
altura = 1.64
peso = 80

imc = peso / altura**2

print(nome)
print('[IMC]:', imc)

# OU

print(f'{nome} tem {altura:.2f}m, pesa {peso}kg e seu IMC é {imc:.2f}')

# OU

print('{} tem {:.2f}m, pesa {}kg e seu IMC é {:.2f}'.format(nome, altura, peso, imc))