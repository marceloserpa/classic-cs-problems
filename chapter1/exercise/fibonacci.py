import math


def fib1(n: int) -> int:
    if(n < 2):
        return n
    return fib1(n -1 ) + fib1(n - 2)


# Binet's formula is an explicit formula used to find the $n$th term of the Fibonacci sequence. 
# It is so named because it was derived by mathematician Jacques Philippe Marie Binet, 
# though it was already known by Abraham de Moivre.
def fib_binet(n: int) -> int:
   v = math.pow((1 + math.sqrt(5)) / 2, n)
   p = math.pow((1 - math.sqrt(5)) / 2, n) 

   return int(1 / math.sqrt(5) * (v - p))