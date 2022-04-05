# Determining GC Content of Multiple Sequences
# Answer to rosalind.info/problems/gc


# General Function for parsing fasta files
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


def gc_content(filename):
    seqs_dict = parse_fasta(filename)
    gc_dict = {}
    for seq in seqs_dict:
        gc_dict[seq] = (seqs_dict[seq].count("G") + seqs_dict[seq].count("C")) / len(seqs_dict[seq]) * 100
    return gc_dict


def max_gc_content(filename):
    gc_dict = gc_content(filename)
    max_gc = max(gc_dict.values())
    max_gc_seq = ""
    # Determining which seq has the highest GC content.
    for seq in gc_dict:
        if gc_dict[seq] == max_gc:
            max_gc_seq = seq
    return max_gc_seq, max_gc  # returns a tuple


print(max_gc_content("rosalind_gc (1).txt"))

