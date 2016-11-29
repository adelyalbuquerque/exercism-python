rna_transcrito = ''

def to_rna(dna):
    rna_transcrito = ''
    for letra in dna:
        if letra == "C":
            rna_transcrito = rna_transcrito + "G"
        elif letra == "G":
            rna_transcrito = rna_transcrito + "C"
        elif letra == "A":
            rna_transcrito = rna_transcrito + "U"
        elif letra == "T":
            rna_transcrito = rna_transcrito + "A"
        elif letra == "X":
            return ''

    return rna_transcrito

