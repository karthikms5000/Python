def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


try:
    n = int(input("Enter a number: "))
    print("The factorial of", n, "is", factorial(n))
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")