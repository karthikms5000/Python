a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

max_val = max(a, b, c)

if a == b == c:
    print("All three numbers are equal:", a)
elif [a, b, c].count(max_val) > 1:
    print("The greatest number appears more than once:", max_val)
else:
    print("The greatest number is:", max_val)