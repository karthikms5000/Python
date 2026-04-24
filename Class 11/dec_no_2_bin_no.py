n = int(input('Enter a number: '))
binary = ""

# Edge case for 0
if n == 0:
    binary = "0"

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary representation:", binary)
