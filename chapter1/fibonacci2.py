from typing import Dict

# Implement memoization technique to avoid recalculate values reducing the recursive calls
# this technique avoid to grow exponentially the number of calls

# initialize with the stop criteria
memo: Dict[int, int] = {0: 0, 1: 1}

# search the position considering that sequence starts with 0
def fib(n: int) -> int:
    print("called = {}".format(n))
    if  n not in memo:
        # recursive block
        memo[n] = fib(n -1 ) + fib(n - 2)
    return memo[n]


print(fib(8))
#0 1 1 2 3 5 8 13 (21) 

print(fib(7))
#0 1 1 2 3 5 8 (13)

print(fib(100))
#0 1 1 2 3 5 8 (13)