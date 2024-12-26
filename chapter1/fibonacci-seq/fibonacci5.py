
# Implementing Fibonacci using a simple loop using tuple destructor

# search the position considering that sequence starts with 0
def fib(n: int) -> int:
    print("Calculating the Fibonacci sequence until {} nth element.".format(n))

    if(n == 0):
        return n

    i: int = 0
    j: int = 1

    for _ in range(1, n):
        print(j)
        j, i = i+j, j # using tuple destructor remove the need to have a temp variable

    return j




print(fib(8))
#0 1 1 2 3 5 8 13 (21) 

print(fib(7))
#0 1 1 2 3 5 8 (13)

print(fib(100))