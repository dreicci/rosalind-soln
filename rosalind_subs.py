# Answer to rosalind.info/problems/subs
# Getting position of substring from a string

file = open("rosalind_subs.txt", "r")
s = file.readline()
t = file.readline()
position = []

for start in range(len(s)-len(t)+1):
    if s[start:(start+len(t))] == t:
        position.append(start+1)
    else:
        None


for i in range(len(position)):
    print(position[i], end=" "),

file.close()