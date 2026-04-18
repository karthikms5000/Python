# Program to find the product of odd digits in a number

num = int(input("Enter an integer: "))

product = 1
found_odd = False

# Work with absolute value to handle negative numbers
for digit in str(abs(num)):
    d = int(digit)
    if d % 2 != 0:  # check if digit is odd
        product *= d
        found_odd = True

if found_odd:
    print("Product of odd digits:", product)
else:
    print("No odd digits found.")