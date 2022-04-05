# Not Yet Done

m, n = input("Insert value for m and n: ").split()
m, n = int(m), int(n)
fib_seq = [1,1]
value = 0

def fibonacci_death(month, live):
    global fib_seq, value

    if month == 1:
        return fib_seq[0]
    elif month == 2:
        return fib_seq[1]

    elif month > 2:
        for i in range(2, month):
            if i >= live:
                value = fib_seq[i-1] + fib_seq[i-2] - 1
            elif i < live:
                value = fib_seq[i-1] + fib_seq[i-2]

            fib_seq.append(value)

    return fib_seq[month - 1]


print(fibonacci_death(m,n))
print(fib_seq)
