# Not yet done

import re

def parse_fasta(filename):
    seq_dict = {}
    current_seq = ""
    with open(filename) as file:
        seq_data = file.readlines()
        for line in seq_data:
            line = line.replace("\n","")
            if line.startswith(">"):
                line = line.replace(">","")
                current_seq = line
                if line not in seq_dict:
                    seq_dict[line] = ""
            else:
                seq_dict[current_seq] += line

    return seq_dict


def find_all_starts(sequence, pattern):  # Index Generator
    index = sequence.find(pattern)
    index_lst = []
    while index != -1:
        index_lst.append(index)
        index = sequence.find(pattern, index + 1)
    return index_lst


def subseq_index(filename):
    seq_dict = parse_fasta(filename)
    # Assumption: There are only two entries in the dictionary
    seq1 = list(seq_dict.values())[0]
    seq2 = list(seq_dict.values())[1]
    sseq_start = find_all_starts(seq1,seq2[0])  # Determines possible starting indices of subsequence
    sseq_index = []




    return


print(subseq_index("test.txt"))
