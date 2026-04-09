def linear_search(list1, key):
    for index, value in enumerate(list1):
        if value == key:
            return index + 1   # keep 1-based position
    return None

list1 = []
maximum = int(input("How many elements in your list? : "))

print("Enter each element and press enter:")
for i in range(maximum):
    n = int(input())
    list1.append(n)

print("The List contents are:", list1)

key = int(input("Enter the number to be searched: "))
position = linear_search(list1, key)

if position is None:
    print("Number", key, "is not present in the list")
else:
    print("Number", key, "is present at position", position)