#!/usr/bin/env python3

fibonacci = []

def fib_seq(a=0, b=1, n=988):
    """ Retuns a list of n fibonacci numbers """
    if (len(fibonacci) > n):
        return fibonacci
    else:
        fibonacci.append(a)
        temp = a
        a = b
        b = b + temp
        fib_seq(a, b, n)

def golden_ratio(precision=988):
    """ Returns an approximation of the golden ratio using above fibonacci """
    fib_seq(n=precision)
    ratio = fibonacci[precision] / fibonacci[(precision-1)]
    return ratio

if __name__=="__main__":
    print(golden_ratio())

