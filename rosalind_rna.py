# Transcription of a DNA seq
# Answer to rosalind.info/problems/rna

dna_seq = ""
def read_seq(filename):
    global dna_seq
    dna_seq = open(filename, "r").read().upper()
    return dna_seq


def transcribe_dna(dna_seq):
    rna = dna_seq.replace("T", "U")
    output = open("transcribed.txt", "a")
    output.write(rna)
    return rna

read_seq("rosalind_rna.txt")
transcribe_dna(dna_seq)

