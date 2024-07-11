hora = input('Que horas são? ')

try:
    hora = float(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora > 11 and hora <= 17:
        print('Boa tarde!')
    elif hora > 17 and hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida')
except:
    print('O valor digitado não é uma hora válida!')
    