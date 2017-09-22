# total number of n's of the sequence to print
f = int(raw_input("How many fibonacci numbers should I print? "))
ns = range(1, f+1)

# definition for finding a fibonacci number
def fibonacci(n):
    fib = [0] * (n + 1)

    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# print each number using above definition
for n in ns:
    print fibonacci(n)
