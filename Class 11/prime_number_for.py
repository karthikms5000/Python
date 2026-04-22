num = int(input("Enter a number: "))

if num < 0:
    print(num, "is negative. Prime numbers are defined only for positive integers greater than 1.")
elif num in (0, 1):
    print(num, "is not a prime number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")