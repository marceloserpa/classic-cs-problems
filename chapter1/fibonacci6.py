
# Generate the entire Fibonacci sequence until N
from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
    print("Calculating the Fibonacci sequence until {} nth element.".format(n))

    yield 0

    if n > 0: yield 1

    i: int = 0
    j: int = 1
    
    for _ in range(1, n):
        i, j = j, j+i
        yield j


for i in fib(50):
    print(i)