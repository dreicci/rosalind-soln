# Answer to rosalind.info/problems/orf
# Function to determine all possible reading frames in a DNA sequence

genetic_code_dna = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }


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


def reverse_complement(dna_seq):
    # reverse = dna_seq[::-1]
    # reverse_dict = reverse.maketrans("AGCT","TCGA")
    # reverse = reverse.translate(reverse_dict)
    reverse = dna_seq[::-1].translate(str.maketrans("AGCT","TCGA"))
    # output = open("output_orf.txt", "a")
    # output.write(reverse)

    return reverse


def find_all_starts(sequence):  # Index Generator
    index = sequence.find("ATG")
    index_lst = []
    while index != -1:
        index_lst.append(index)
        index = sequence.find("ATG", index + 1)
    return index_lst


def dna_translate(sequence):
    # rna_txt = open(file, "r")
    # rna_seq = rna_txt.read()
    orf = []

    for starting_index in find_all_starts(sequence):
        protein_seq = ""
        for index in range(starting_index, len(sequence) - 3, 3):
            # if sequence[index:index + 3] in genetic_code_dna.keys():
            if genetic_code_dna[sequence[index:index + 3]] != '_':
                protein_seq += genetic_code_dna[sequence[index:index + 3]]
            else:
                orf.append(protein_seq)
                break
    # rna_txt.close()
    return orf


seq_dict = parse_fasta("rosalind_orf.txt").items()
seq_data = [value for key, value in seq_dict]
seq_orig = seq_data[0]
seq_revc = reverse_complement(seq_orig)
orf = list(dict.fromkeys(dna_translate(seq_orig) + dna_translate(seq_revc)))
for prot_seq in orf:
    print(prot_seq)
