from functools import lru_cache

# lru_cache allows to automatically apply memoization to our function

# search the position considering that sequence starts with 0
@lru_cache(maxsize=None)
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

print(fib(100))
#0 1 1 2 3 5 8 (13)