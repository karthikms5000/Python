def binary_search(arr, key):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def create_list():
    arr = []
    print("Enter numbers (any order). Type 'stop' to finish:")

    while True:
        user_input = input()

        if user_input.lower() == 'stop':
            break

        try:
            arr.append(int(user_input))
        except ValueError:
            print("Invalid input! Enter an integer or 'stop'.")

    arr.sort()
    print("Sorted list:", arr)
    return arr


# Main program
arr = []

while True:
    print("\nMENU")
    print("1. Create new list")
    print("2. Display list")
    print("3. Search element")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        arr = create_list()

    elif choice == '2':
        if arr:
            print("Current list:", arr)
        else:
            print("List is empty. Create a list first.")

    elif choice == '3':
        if not arr:
            print("List is empty. Create a list first.")
            continue

        try:
            key = int(input("Enter number to search: "))
            pos = binary_search(arr, key)

            if pos != -1:
                print(f"{key} found at position {pos + 1}")
            else:
                print(f"{key} not found")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1–4.")