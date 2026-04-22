num = int(input("Enter a number: "))

if num < 0:
    print(num, "is negative. Prime numbers are defined only for positive integers greater than 1. So it is not a prime number.")
elif num in (0, 1):
    print(num, "is not a prime number.")
else:
    i = 2
    while i <= int(num ** 0.5):
        if num % i == 0:
            print(num,"is not a prime number.")
            break
        i += 1
    else:
        print(num,"is a prime number.")
