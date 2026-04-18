def analyze_numbers(numbers):
    if not numbers:
        return "No numbers provided."

    numbers.sort()  # sorts in ascending order
    max_val = numbers[-1]
    count = numbers.count(max_val)

    if count == len(numbers):
        result = "All numbers are equal:", max_val
    elif count > 1:
        result = "The greatest number appears", count, "times:", max_val
    else:
        result = "The greatest number is:", max_val

    return result, numbers


# Taking input line-by-line
numbers = []
print("Enter numbers one by one. Type 'done' to finish:")

while True:
    user_input = input("> ")
    if user_input.lower() == "done":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

result, sorted_numbers = analyze_numbers(numbers)

print(result)
print("Sorted numbers:", sorted_numbers)