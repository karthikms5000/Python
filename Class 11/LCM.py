from math import lcm

while True:
    try:
        user_input = input("\nEnter numbers (or type 'exit'): ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        nums = list(map(int, user_input.split()))
        
        if not nums:
            print("Enter at least one number.")
            continue
        
        result = 1
        for n in nums:
            result = lcm(result, abs(n))
        
        print("LCM:", result)

    except ValueError:
        print("Invalid input! Use only integers.")