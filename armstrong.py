n=int(input("enter the n value"))
def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == n
result=is_armstrong_number(n)
print(result)