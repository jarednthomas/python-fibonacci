#!/usr/bin/env python3
fibonacci = []

def fib_seq(a=0, b=1, n=20):
    """ Retuns a list of n fibonacci numbers """
    if (len(fibonacci) > n):
        return fibonacci
    else:
        fibonacci.append(a)
        temp = a
        a = b
        b = b + temp
        fib_seq(a, b, n)

if __name__=="__main__":
    fib_seq()
    print(fibonacci)
