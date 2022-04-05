# Answer to rosalind.info/problems/perm
# Function which lists out all the total permutations possible given <n> entities


import itertools
file = open("rosalind_perm.txt", "r")
n = int(file.read())

def calc_perms(length):
    total = 1
    for num in range(1, length + 1):
        total = total * num
    return total

def list_perms(length):
    list1 = []
    perm = []
    a = 1
    for a in range(1, length + 1):
        perm.append(a)

    list1 = list(itertools.permutations(perm))


    for combination in list1:  # Printing all perms
        for number in combination:
            print(number, end=" ")
        print()
    return


print(calc_perms(n))
list_perms(n)

""" Algorithmic solution: https://www.geeksforgeeks.org/combinations-in-python-without-using-itertools/
n=7

def permutations(l):
    return [ (m[:i] + [l[0]] + m[i:]) for m in permutations(l[1:]) for i in xrange(len(m)+1) ] if len(l)>1 else [l]

p = permutations(range(1,n+1))

print len(p)
for l in p:
    print ' '.join(map(str,l))
"""
