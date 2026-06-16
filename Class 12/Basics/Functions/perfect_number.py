import math

def is_perfect_number(n):
    if n < 2:
        return False

    divisor_sum = 1

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            divisor_sum += i
            pair = n // i

            if pair != i:
                divisor_sum += pair

    return divisor_sum == n

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")