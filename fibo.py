# Fibonacci numbers module

def fib(n):   # write Fibonacci series up to n
    e, f = 0, 1
    while f < n:
        print(f, end=' ')
        e, f = f, e+f
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


