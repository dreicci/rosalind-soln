# Recurrence Relations
# Answer to rosalind.info/problems/fib


def fibonacci_number(month, litter):
    if month == 1:
        return 1
    elif month == 2:
        return 1
    elif month > 2:
        return fibonacci_number(month - 1, litter) + fibonacci_number(month - 2, litter) * month


with open("rosalind_fib.txt") as file:
    month, litter = file.read().split()
    month, litter = int(month), int(litter)
    print(fibonacci_number(month, litter))
