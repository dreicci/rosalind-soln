# Getting the consensus sequence given 10 sequences of the same length.
# Answer to rosalind.info/problems/cons/

profile = [['A', 'C', 'G', 'T']]
consensus_seq = ""

# General function for parsing FASTA files. Output is a dictionary of sequences
def parse_fasta(filename):
    seq_dict = {}
    current_seq = ""
    with open(filename) as file:
        seq_data = file.readlines()
        for line in seq_data:
            line = line.rstrip()
            if line.startswith(">"):
                line = line.replace(">","")
                current_seq = line
                if line not in seq_dict:
                    seq_dict[line] = ""
            else:
                seq_dict[current_seq] += line

    return seq_dict


seq_list = list(parse_fasta("rosalind_cons.txt").values())  # Retrieves all sequences and gather in a list

for sequence in range(len(seq_list)):   # A loop which separates each base in the sequence as an element of a list
    seq_list[sequence] = list(seq_list[sequence])



for i in range(len(seq_list[0])):
    # Resetting nucleotide counter
    a = 0
    g = 0
    c = 0
    t = 0
    for sequence in seq_list:
        if sequence[i] == 'A':
            a += 1
        elif sequence[i] == 'G':
            g += 1
        elif sequence[i] == 'C':
            c += 1
        elif sequence[i] == 'T':
            t += 1
    profile.append([a,c,g,t])


profile_matrix = [[profile[i][j] for i in range(len(profile))] for j in range(len(profile[0]))]  # Transposing matrix to 4 x n format

for i in range(1, len(profile)):  # Getting Concensus Sequence by finding maximum in each list in profile and getting the index of it to get respective nucleotide.
    consensus_seq += profile[0][profile[i].index(max(profile[i]))]
print(consensus_seq)

for i in range(len(profile_matrix)):  # Printing colon in nucleotide sequence
    profile_matrix[i][0] += ':'

for i in range(len(profile_matrix)):
    for j in range(len(profile_matrix[i])):
        print(profile_matrix[i][j], end=" ")
    print()
