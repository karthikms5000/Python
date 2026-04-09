def hash_insert(table, value):
    size = len(table)
    index = value % size

    # Linear probing
    for _ in range(size):
        if table[index] is None:
            table[index] = value
            return
        index = (index + 1) % size

    print("Hash table is full!")


def hash_find(table, key):
    size = len(table)
    index = key % size

    # Linear probing
    for _ in range(size):
        if table[index] is None:
            return None
        if table[index] == key:
            return index  # 0-based index
        index = (index + 1) % size

    return None


# Main
hash_table = [None] * 10
values = [34, 16, 2, 93, 80, 77, 51]

for v in values:
    hash_insert(hash_table, v)

print("Hash table:", hash_table)

# Search
try:
    key = int(input("Enter number to search: "))
    pos = hash_find(hash_table, key)

    if pos is None:
        print(f"{key} not found")
    else:
        print(f"{key} found at index {pos}")

except ValueError:
    print("Please enter a valid integer")