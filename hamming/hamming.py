
def distance(sequencia_1, sequencia_2):
    contador = 0
    if len(sequencia_1) != len(sequencia_2):
        raise ValueError('Sequences with diferents size')
    for index, letter in enumerate(sequencia_1):
        if letter != sequencia_2[index]:
            contador = contador + 1
    return contador
