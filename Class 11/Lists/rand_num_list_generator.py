from random import randint

while True:
    try:
        minimum = int(input("Min: "))
        maximum = int(input("Max: "))

        if minimum > maximum:
            print("Min cannot be greater than Max.")
            continue

        n = int(input("Numbers limit: "))
        if n <= 0:
            print("Numbers limit must be greater than 0.")
            continue

        break  # all inputs are valid

    except ValueError:
        print("Please enter valid integers only.")

a = []
for _ in range(n):
    a.append(randint(minimum, maximum))

print(a)
