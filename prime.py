import math
# n=int(input('ENTER THE N VALUE'))
p=set()
def is_prime(n):
    if n <= 1:
        return
    if n <= 3:
        p.add(n)
        return n
    if n % 2 == 0 or n % 3 == 0:
        return
    for i in range(5, int(math.isqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return
    p.add(n)
    return n
for i in range(0,100):
    is_prime(i)  
print(p)