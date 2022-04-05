# Counting Base Pairs in a DNA sequence
# Answer to rosalind.info/problems/dna


def base_count(filename):
    with open(filename) as file:
        seq_str = file.read().upper()  # Converts all bases to uppercase in case that there are mix of upper and lowercases in the sequence.
        a, g, c, t = seq_str.count("A"), seq_str.count("G"), seq_str.count("C"), seq_str.count("T")

    return a, g, c, t


print(base_count("rosalind_dna.txt"))
