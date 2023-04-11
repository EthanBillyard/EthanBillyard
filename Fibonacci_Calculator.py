#allows the program to time how long it takes to compute
import time
start = time.time()

def Fib(n):
    if n <= 1:
        return n
    else:
        return (Fib(n-1) + Fib(n-2))

fibonacciTerms = int(input("How many terms do you want: "))
print(Fib(fibonacciTerms))

end = time.time()
print(end - start, "seconds")