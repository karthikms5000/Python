def fibonacci(n):
    if n <= 0:
        print("Please enter a positive number of terms.")
        return

    f1, f2 = 0, 1
    count = 0

    print("Fibonacci series:", end=" ")

    while count < n:
        print(f1, end=" ")
        f1, f2 = f2, f1 + f2
        count += 1

# Take input
n = int(input("Enter the number of terms: "))
fibonacci(n)
