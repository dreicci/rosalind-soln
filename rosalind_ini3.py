# Getting the sum of odd numbers from input a  to b

import math
a = 0
b = 0
sum = 0



def sum_of_odds(a, b):
    global sum
    if a % 2 != 1:  # check if even
        a += 1
    while a <= b:
        sum += a
        a += 2
    print(sum)
    return

a, b = input("Insert the range: ").split()
a, b = int(a), int(b)
sum_of_odds(a,b)