import math
n=int(input('ENTER THE N VALUE'))
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.isqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
result=is_prime(n)
print(result)