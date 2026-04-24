#Calculate sum of digits of a random 3 digit number
from random import randint

n = randint(100, 999)
print("The number is", n)

print("The sum of the digits is", n // 100 + (n // 10) % 10 + n % 10)
