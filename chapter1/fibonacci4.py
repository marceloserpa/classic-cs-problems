
# Implementing Fibonacci using a simple loop

# search the position considering that sequence starts with 0
def fib(n: int) -> int:
    print("Calculating the Fibonacci sequence until {} nth element.".format(n))

    # stop criteria
    if(n == 0):
        return n

    i: int = 0
    j: int = 1
    temp: int = 0 # used to swap j to i

    for _ in range(1, n):
        print(j)
        temp = j
        j = i + j
        i = temp

    return j




print(fib(8))
#0 1 1 2 3 5 8 13 (21) 

print(fib(7))
#0 1 1 2 3 5 8 (13)

print(fib(100))