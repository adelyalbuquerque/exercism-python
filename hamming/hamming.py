
def distance(sequencia_1, sequencia_2):
    contador = 0
    if len(sequencia_1) != len(sequencia_2):
        raise ValueError('Sequences with diferents size')
    for letter_seq_1, letter_seq_2 in  zip(sequencia_1, sequencia_2):
        if letter_seq_1 != letter_seq_2:
            contador = contador + 1
    return contador
