# Slicing a string from a to b, inclusive, and c to d, inclusive.

import math
a = 0
b = 0
c = 0
d = 0
s = ""

'''
def readf(filename):
    global s,a,b,c,d
    file_ref = open(filename, 'r')
    lines = file_ref.readlines()
    s = lines[0]
    a,b,c,d = lines[1].split()
    file_ref.close()
    return
'''

def slice_string(a,b,c,d):
    # readf("ini2.txt")
    text1 = s[a:b+1]
    text2 = s[c:d+1]

    print(text1 + " " + text2)
    return

s = input("Copy String: ")
a, b, c, d = input("Value of Two legs (separated by ', '): ").split()
a,b,c,d = int(a), int(b), int(c), int(d)
slice_string(a,b,c,d)

'''
Alternate Solution:
infile = open('stringsAndLists.txt')
string1 = infile.readline()
string2 = infile.readline()
string2 = string2.split(' ')
a=int(string2[0])
b=int(string2[1])
c=int(string2[2])
d=int(string2[3])
print string1[a:b+1], string1[c:d+1]
'''



