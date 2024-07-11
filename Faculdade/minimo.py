# Retornar o menor elemento de uma lista

def calc_min(list):
    min = list[0]
    for element in list:
        if (element < min):
            min = element
    return min

numList = [89, 26, 56, 12, 5, 65, 98, 2, 78]
print(f'A lista enviada é {numList} e o valor mínimo é {calc_min(numList)}')
    