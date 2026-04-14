def fibonacci(n):
    if n <= 0:
        print("Please enter a positive number of terms.")
        return

    f1, f2 = 0, 1
    print("Fibonacci series:", end=" ")

    for _ in range(n):
        print(f1, end=" ")
        f1, f2 = f2, f1 + f2

# Take input
n = int(input("Enter the number of terms: "))
fibonacci(n)
