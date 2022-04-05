# Word counting given a string input

sentence = input("Insert string: ")
dict = {}

for word in sentence.split():
    if word not in dict:
        dict[word] = 1
    elif word in dict:
        dict[word] += 1


for key, value in dict.items():
    key , value = str(key), str(value)
    print(key + " " + value)