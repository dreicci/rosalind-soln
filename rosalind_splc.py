# Returns a protein sequence given pre-mRNA and its set of introns
# Answer to rosalind.info/problems/splc

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
        'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
        'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W',
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


def find_all_starts(sequence):  # Index Generator for Multiple Reading Frames
    index = sequence.find("ATG")
    index_lst = []
    while index != -1:
        index_lst.append(index)
        index = sequence.find("ATG", index + 1)
    return index_lst


def dna_translate(sequence):  # Expected Input: DNA Sequence
    orf = []
    starting_index = sequence.find("ATG")  # Assumption: Only one starting index
    protein_seq = ""
    for index in range(starting_index, len(sequence), 3):
        # if sequence[index:index + 3] in genetic_code_dna.keys(): - in case there are anomalies in DNA Seq.
        if genetic_code_dna[sequence[index:index + 3]] != 'STOP':
            protein_seq += genetic_code_dna[sequence[index:index + 3]]
        else:
            orf.append(protein_seq)

    # rna_txt.close()
    return orf  # Returns list of all reading frames of a sequence (excluding its reverse complement)


def splice_rna(seq_dict):  # Expected Input: {DNA1: Seq of Interest, DNA2: Intron 1, DNA3: Intron 2...}
    exon = list(seq_dict.values())[0]
    introns = [intron for intron in list(seq_dict.values())[1:]]  # Creates a list of all introns
    for intron in introns:  # Looping through all introns to replace w/ ""
        exon = exon.replace(intron, "")

    return exon


def print_prot_seq(prot_seq_lst):  # Printing protein seq in terminal (One line for each sequence)
    for index in range(len(prot_seq_lst)):
        print(prot_seq_lst[index])
        print()
    return


seq_dict = parse_fasta("rosalind_splc.txt")
exon = splice_rna(seq_dict)
prot_seq = dna_translate(exon)
print_prot_seq(prot_seq)

