# Answer to rosalind.info/problems/revp
# Determining palindromic sequences from its position and length


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


def reverse_complement(dna_seq):
    # reverse = dna_seq[::-1]
    # reverse_dict = reverse.maketrans("AGCT","TCGA")
    # reverse = reverse.translate(reverse_dict)
    reverse = dna_seq[::-1].translate(str.maketrans("AGCT","TCGA"))
    # output = open("output_revc.txt", "a")
    # output.write(reverse)

    return reverse


seq_list = list(parse_fasta("rosalind_revp (2).txt").values())
revc_seq = ""
for seq in seq_list:
    revc_seq = reverse_complement(seq)


seq = seq_list[0]
reverse = revc_seq[::-1]
# print("5' ", seq, " 3'")
# print("3' ", reverse, " 5'")
# print("3' ",reverse[6:4:-1], " 5'")
# print(len(seq))

# print(seq[4:8])
# print(reverse[7:3:-1])
list = []

for length in range(4, 13):
    for x in range(len(seq)-length+1):
        if seq[x:x+length] == reverse[x+length-1:x-1:-1]:
            list.append((x+1, length))

for item in list:
    print(item[0],"\t", item[1])

