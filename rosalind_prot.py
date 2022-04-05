# Answer to rosalind.info/problems/prot
# Function which translates an mRNA sequence to AA sequence

genetic_code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


def rna_translate(file):
    protein_seq = ""
    rna_txt = open(file, "r")
    rna_seq = rna_txt.read()
    start = rna_seq.find("AUG")
    for index in range(start, len(rna_seq), 3):
        if rna_seq[index:index + 3] in genetic_code.keys():
            if genetic_code[rna_seq[index:index + 3]] != "STOP":
                protein_seq += genetic_code[rna_seq[index:index + 3]]
    rna_txt.close()
    return protein_seq


print(rna_translate("rosalind_prot.txt"))
