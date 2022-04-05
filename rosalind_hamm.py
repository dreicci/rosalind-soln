# Finding difference between two aligned sequences of same length
# Answer to rosalind.info/problems/hamm


file = open("rosalind_hamm.txt", "r")
s = file.readline()
t = file.readline()


def diff(seq1, seq2):
    diff = 0
    for pos in range(min(len(seq1),len(seq2))):
        if seq1[pos] != seq2[pos]:
            diff += 1
    return diff


print(diff(s,t))
