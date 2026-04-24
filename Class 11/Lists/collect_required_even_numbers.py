required_even_num = int(input("Enter the number of even numbers: "))
even_numbers = []
while len(even_numbers) < required_even_num:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_numbers.append(num)
print("The list is: ", even_numbers)