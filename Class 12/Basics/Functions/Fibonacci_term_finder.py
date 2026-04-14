#This code calculates the Fibonacci number for a given term number. It uses 0-based indexing, meaning that the 0th term is 0, the 1st term is 1, and so on.
def fibonacci(n):
    if n < 0:
        raise ValueError("Please enter a non-negative integer.")
    elif n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


try:
    n = int(input("Enter the term number: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    try:
        print("Fibonacci value:", fibonacci(n))
    except ValueError as e:
        print(e)