# Input: Three-digit number
num = int(input("Enter a three-digit number: "))

if 100 <= num <= 999:
    # Initialize variables
    sum_of_cubes = 0
    original_num = num
    
    # Extract digits and calculate the sum of cubes using a while loop
    while num > 0:
        digit = num % 10  # Extract the last digit
        sum_of_cubes += digit ** 3  # Add the cube of the digit to the sum
        num //= 10  # Remove the last digit
    
    # Check if the sum of cubes is equal to the original number
    if sum_of_cubes == original_num:
        print(original_num,"is an Armstrong number.")
    else:
        print(original_num,"is not an Armstrong number.")
else:
    print("Please enter a valid three-digit number.")
