def translate_dna(in_protein:str)->str:
    out_protein = ""
    if in_protein == "A":
        out_protein = "T"
    elif in_protein == "T":
        out_protein = "A"
    elif in_protein == "C":
        out_protein = "G"
    elif in_protein == "G":
        out_protein = "C"

    return out_protein
