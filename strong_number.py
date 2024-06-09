import math
n=int(input("enter the n value"))
def is_strong_number(n):
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(n))
    return sum_of_factorials == n
result=is_strong_number(n)
print(result)