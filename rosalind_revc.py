# Function which determines the reverse complement of a DNA sequence in a 5'-3' direction
# Answer to rosalind.info/problems/revc


dna_seq = ""


def read_seq(filename):
    global dna_seq
    dna_seq = open(filename, "r").read().upper()
    return dna_seq


def reverse_complement(dna_seq):
    # reverse = dna_seq[::-1]
    # reverse_dict = reverse.maketrans("AGCT","TCGA")
    # reverse = reverse.translate(reverse_dict)
    reverse = dna_seq[::-1].translate(str.maketrans("AGCT","TCGA"))
    output = open("output_revc.txt", "a")
    output.write(reverse)

    return

read_seq("rosalind_revc.txt")
reverse_complement(dna_seq)
