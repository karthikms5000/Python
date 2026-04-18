def find_greatest(numbers):
    if not numbers:
        return "No numbers provided."

    max_val = max(numbers)
    count = numbers.count(max_val)

    if count == len(numbers):
        return "All numbers are equal:", max_val
    elif count > 1:
        return "The greatest number appears", count, "times:", max_val
    else:
        return "The greatest number is:", max_val
    
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print(find_greatest(numbers))