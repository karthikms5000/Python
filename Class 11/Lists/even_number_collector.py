even_numbers = []
limit = int(input("Number limit: "))
count = 0
while count < limit:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_numbers.append(num)
    count += 1
print("The list of even numbers is:", even_numbers)