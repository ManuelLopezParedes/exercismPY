def to_rna(dna_strand):
    lista = ""
    trans= {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    for dna in dna_strand:
        lista += trans[dna]
    return lista