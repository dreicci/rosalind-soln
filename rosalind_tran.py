# Determines the transition / transverse ratio of mutation given two aligned sequences of same length.
# Answer to rosalind.info/problems/tran

def parse_fasta(filename):
    seq_dict = {}
    current_seq = ""
    file = open(filename, "r")
    seq_data = file.read()
    for line in seq_data.splitlines():
        if line.startswith(">"):
            line = line.replace(">","")
            current_seq = line
            if line not in seq_dict:
                seq_dict[line] = ""
        else:
            seq_dict[current_seq] += line
    file.close()
    return seq_dict



def tran_ratio(two_seq_dict):  # Expected Input: Dictionary containing two sequences
    # This dictionary will be used to determine whether transverse or transition kind of mutation.
    nucleotide = {'A': 0,
                  'G': 1,
                  'C': 3,
                  'T': 4}
    first_seq = list(two_seq_dict.values())[0]
    second_seq = list(two_seq_dict.values())[1]
    trans, tranv = 0., 0.
    for pos in range(len(first_seq)):
        if first_seq[pos] != second_seq[pos]:
            if abs(nucleotide[first_seq[pos]] - nucleotide[second_seq[pos]]) == 1:
                trans += 1
            elif abs(nucleotide[first_seq[pos]] - nucleotide[second_seq[pos]]) > 1:
                tranv += 1

    ratio = trans / tranv
    return ratio

two_seq_dict = parse_fasta("rosalind_tran.txt")
print(tran_ratio(two_seq_dict))
