# Extracting even-numbered lines to a new file

filename = "ini2.txt"
input = open(filename, "r")
output = open("output.txt", "a")
for line in input.read().splitlines()[1::2]:
    output.write(line+"\n")

output.close()
print(input.read().splitlines())