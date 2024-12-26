
# search the position considering that sequence starts with 0
def fib(n: int) -> int:
    print("called = {}".format(n))
    # stop criteria
    if(n < 2):
        return n

    # recursive block
    return fib(n -1 ) + fib(n - 2)


print(fib(8))
#0 1 1 2 3 5 8 13 (21) 

print(fib(7))
#0 1 1 2 3 5 8 (13)


# this algorithm grows exponentially
# to calculate 4 the fib method is called 9 times
# to calculate 10 the fib method is called 21.891 times


