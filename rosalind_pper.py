# Answer to rosalind.info/problems/pper
# All permutations possible choosing <b> entities from <a> entities

with open("rosalind_pper (1).txt") as f:
    a, b = f.read().split()
    a, b = int(a), int(b)


def partial_perm():
    perm = 1
    global a, b
    for i in range(a-b+1, a+1, 1):
        perm = perm * i % 1E6
    return int(perm)


print(partial_perm())
