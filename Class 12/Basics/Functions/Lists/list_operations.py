def get_int(prompt):
    """Safely get an integer input."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def print_list(lst):
    print("\nCurrent list:", lst)


# -------- Accessing & Traversing --------
def access_element(lst):
    index = get_int("Enter index: ")
    if index is None:
        return
    if -len(lst) <= index < len(lst):
        print("Element:", lst[index])
    else:
        print("Invalid index")


def traverse_list(lst):
    print("List elements:", end=" ")
    for item in lst:
        print(item, end=" ")
    print()


def slice_list(lst):
    start = get_int("Start index: ")
    end = get_int("End index: ")
    if start is None or end is None:
        return
    print("Sliced list:", lst[start:end])


# -------- Adding Elements --------
def append_element(lst):
    val = get_int("Enter element to append: ")
    if val is not None:
        lst.append(val)


def extend_list(lst):
    try:
        new_list = list(map(int, input("Enter list to extend: ").split()))
        lst.extend(new_list)
    except ValueError:
        print("Invalid input")


def insert_element(lst):
    val = get_int("Enter element: ")
    pos = get_int("Enter position: ")
    if val is None or pos is None:
        return
    lst.insert(pos, val)


def concatenate_list(lst):
    try:
        new_list = list(map(int, input("Enter another list: ").split()))
        print("Concatenated list:", lst + new_list)
    except ValueError:
        print("Invalid input")


def replicate_list(lst):
    times = get_int("Enter repetitions: ")
    if times is not None:
        print("Replicated list:", lst * times)


# -------- Removing Elements --------
def clear_list(lst):
    lst.clear()
    print("List cleared.")


def pop_element(lst):
    if not lst:
        print("List is empty")
        return
    pos = get_int("Enter index to pop: ")
    if pos is None:
        return
    if -len(lst) <= pos < len(lst):
        print("Popped:", lst.pop(pos))
    else:
        print("Invalid index")


def remove_element(lst):
    val = get_int("Enter element to remove: ")
    if val is None:
        return
    if val in lst:
        lst.remove(val)
    else:
        print("Element not found")


def remove_all(lst):
    val = get_int("Enter element to remove: ")
    if val is None:
        return
    lst[:] = [x for x in lst if x != val]


def delete_by_index(lst):
    pos = get_int("Enter index to delete: ")
    if pos is None:
        return
    if -len(lst) <= pos < len(lst):
        del lst[pos]
    else:
        print("Invalid index")


def remove_odds(lst):
    lst[:] = [x for x in lst if x % 2 == 0]


def remove_negatives(lst):
    lst[:] = [x for x in lst if x >= 0]


def remove_duplicates(lst):
    lst[:] = list(dict.fromkeys(lst))


# -------- Modifying --------
def modify_element(lst):
    pos = get_int("Enter index: ")
    if pos is None:
        return
    if -len(lst) <= pos < len(lst):
        val = get_int("Enter new value: ")
        if val is not None:
            lst[pos] = val
    else:
        print("Invalid index")


def copy_list(lst):
    list2 = lst.copy()
    print("Copied list:", list2)


# -------- Searching --------
def membership_test(lst):
    val = get_int("Enter element: ")
    if val is not None:
        print(val, "is in list" if val in lst else "not in list")


def find_index(lst):
    val = get_int("Enter element: ")
    if val is None:
        return
    if val in lst:
        print("Index:", lst.index(val))
    else:
        print("Not found")


def count_occurrence(lst):
    val = get_int("Enter element: ")
    if val is not None:
        print("Occurrences:", lst.count(val))


def linear_search(lst):
    val = get_int("Enter element: ")
    if val is None:
        return
    for i in range(len(lst)):
        if lst[i] == val:
            print("Found at index:", i)
            return
    print("Not found")


# -------- Sorting --------
def reverse_list(lst):
    lst.reverse()


def sort_new(lst):
    print("Sorted (new list):", sorted(lst))


def sort_list(lst):
    order = input("Enter 'asc' or 'desc': ").strip().lower()
    if order == "asc":
        lst.sort()
    elif order == "desc":
        lst.sort(reverse=True)
    else:
        print("Invalid choice")


# -------- Math --------
def show_stats(lst):
    if not lst:
        print("List is empty")
        return
    print("Max:", max(lst))
    print("Min:", min(lst))
    print("Sum:", sum(lst))
    print("Count:", len(lst))


# -------- Menu System --------
def main():
    try:
        lst = list(map(int, input("Enter elements: ").split()))
    except ValueError:
        print("Invalid input. Starting with empty list.")
        lst = []

    while True:
        print_list(lst)

        print("""
1. Access / Traverse
2. Add Elements
3. Remove Elements
4. Modify
5. Search
6. Sort
7. Math Operations
0. Exit
""")

        choice = get_int("Enter choice: ")
        if choice is None:
            continue

        if choice == 0:
            print("Exiting...")
            break

        elif choice == 1:
            print("1.Access 2.Traverse 3.Slice")
            sub = get_int("Choice: ")
            if sub == 1:
                access_element(lst)
            elif sub == 2:
                traverse_list(lst)
            elif sub == 3:
                slice_list(lst)

        elif choice == 2:
            print("1.Append 2.Extend 3.Insert 4.Concat 5.Replicate")
            sub = get_int("Choice: ")
            if sub == 1:
                append_element(lst)
            elif sub == 2:
                extend_list(lst)
            elif sub == 3:
                insert_element(lst)
            elif sub == 4:
                concatenate_list(lst)
            elif sub == 5:
                replicate_list(lst)

        elif choice == 3:
            print("1.Clear 2.Pop 3.Remove 4.Remove All 5.Delete Index 6.Remove Odds 7.Remove Negatives 8.Remove Duplicates")
            sub = get_int("Choice: ")
            if sub == 1:
                clear_list(lst)
            elif sub == 2:
                pop_element(lst)
            elif sub == 3:
                remove_element(lst)
            elif sub == 4:
                remove_all(lst)
            elif sub == 5:
                delete_by_index(lst)
            elif sub == 6:
                remove_odds(lst)
            elif sub == 7:
                remove_negatives(lst)
            elif sub == 8:
                remove_duplicates(lst)

        elif choice == 4:
            print("1.Modify 2.Copy")
            sub = get_int("Choice: ")
            if sub == 1:
                modify_element(lst)
            elif sub == 2:
                copy_list(lst)

        elif choice == 5:
            print("1.Member 2.Index 3.Count 4.Linear Search")
            sub = get_int("Choice: ")
            if sub == 1:
                membership_test(lst)
            elif sub == 2:
                find_index(lst)
            elif sub == 3:
                count_occurrence(lst)
            elif sub == 4:
                linear_search(lst)

        elif choice == 6:
            print("1.Reverse 2.Sorted(New) 3.Sort")
            sub = get_int("Choice: ")
            if sub == 1:
                reverse_list(lst)
            elif sub == 2:
                sort_new(lst)
            elif sub == 3:
                sort_list(lst)

        elif choice == 7:
            show_stats(lst)

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()