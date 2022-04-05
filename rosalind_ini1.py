# Computing for the square of hypoteneuse given two legs.

import math
a = 0
b = 0
hypoteneuse = 0

def ask_for_legs():
    global a,b
    a, b = input("Value of Two legs (separated by ', '): ").split()
    a,b = int(a), int(b)
    return

def compute_hypoteneuse(a,b):
    global hypoteneuse
    hypoteneuse = math.sqrt(a*a+b*b)
    print(int(hypoteneuse*hypoteneuse))
    return

ask_for_legs()
compute_hypoteneuse(a,b)



