list1 = list(map(int, input("Enter elements separated by space: ").split()))
while True:
    print("\n========== LIST OPERATIONS MENU ==========")

    print("\n\n==== Accessing & Traversing Elements ====")

    print("1. Access an element by index")
    print("2. Traverse the list")
    print("3. Slicing")

    print("\n\n==== Adding Elements to a List ====")

    print("4. Append an element")
    print("5. Extend the list")
    print("6. Insert an element at a position")
    print("7. Concatenation")
    print("8. Replication")

    print("\n\n==== Removing Elements from a List ====")

    print("9. Clear all elements")
    print("10. Pop an element")
    print("11. Remove an element")
    print("12. Remove all occurrences of an element")
    print("13. Delete using del")
    print("14. Delete all odd numbers")
    print("15. Delete all negative numbers")
    print("16. Remove duplicates")

    print("\n\n==== Modifying Elements in a List ====")

    print("17. Modify element using index")
    print("18. Copy list to list2")

    print("\n\n==== Searching & Membership ====")

    print("19. Membership testing")
    print("20. Find index of an element")
    print("21. Occurrence of a number")
    print("22. Linear search")
    print("23. Find common elements with another list")

    print("\n\n==== Sorting & Ordering ====")

    print("24. Reverse the list")
    print("25. Sorted (returns new list)")
    print("26. Sort ascending or descending")
    print("27. Count total elements")

    print("\n\n==== Mathematical Operations ====")

    print("28. Max element")
    print("29. Min element")
    print("30. Sum of elements")
    print("31. Largest, second largest, third largest")
    print("32. Compare with another list")
    
    print("\n33. Print the list")
    print("0. EXIT")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Enter a valid number")
        continue

    choice = int(choice)

    if choice == 0:
        print("Exiting program...")
        break

    elif choice == 1:
        index = int(input("Enter index: "))
        if -len(list1) <= index < len(list1):
            print("Element:", list1[index])
        else:
            print("Invalid index")

    elif choice == 2:
        print("List elements:")
        for item in list1:
            print(item, end=" ")

    elif choice == 3:
        start_index = int(input("Start index: "))
        end_index = int(input("End index: "))
        print("Sliced list:", list1[start_index:end_index])

    elif choice == 4:
        element = int(input("Enter element to append: "))
        list1.append(element)
        print("Updated list:", list1)

    elif choice == 5:
        new_list = list(map(int, input("Enter list to extend: ").split()))
        list1.extend(new_list)
        print("Updated list:", list1)

    elif choice == 6:
        element = int(input("Enter element: "))
        position = int(input("Enter position: "))
        list1.insert(position, element)
        print("Updated list:", list1)

    elif choice == 7:
        new_list = list(map(int, input("Enter another list: ").split()))
        print("Concatenated list:", list1 + new_list)

    elif choice == 8:
        repetitions = int(input("Enter number of repetitions: "))
        print("Replicated list:", list1 * repetitions)

    elif choice == 9:
        list1.clear()
        print("List cleared.")

    elif choice == 10:
        position = int(input("Enter index to pop: "))
        if list1 and -len(list1) <= position < len(list1):
            print("Popped element =", list1.pop(position))
        else:
            print("Invalid index or empty list")
        print("Updated list:", list1)
       
    elif choice == 11:
        element = int(input("Enter element to remove: "))
        if element in list1:
            list1.remove(element)
            print("Updated list:", list1)
        else:
            print("Element not found")

    elif choice == 12:
        element = int(input("Enter element to remove: "))
        list1 = [num for num in list1 if num != element]
        print("Updated list:", list1)

    elif choice == 13:
        position = int(input("Enter index to delete: "))
        if -len(list1) <= position < len(list1):
            del list1[position]
            print("Updated list:", list1)
        else:
            print("Invalid index")

    elif choice == 14:
        list1 = [x for x in list1 if x % 2 == 0]
        print("After deleting odd numbers:", list1)

    elif choice == 15:
        list1 = [x for x in list1 if x >= 0]
        print("Updated list after deleting negative numbers:", list1)

    elif choice == 16:
        list1 = list(dict.fromkeys(list1))
        print("Updated list after removing duplicates:", list1)

    elif choice == 17:
        position = int(input("Enter index to modify: "))
        if -len(list1) <= position < len(list1):
            new_value = int(input("Enter new value: "))
            list1[position] = new_value
            print("Updated list:", list1)
        else:
            print("Invalid index")    

    elif choice == 18:
        list2 = list1.copy()
        print("Copied list (list2):", list2)
    
    elif choice == 19:
        element = int(input("Enter element to check: "))
        print(element, "is in list" if element in list1 else "not in list")

    elif choice == 20:
        element = int(input("Enter element: "))
        if element in list1:
            print("Index =", list1.index(element))
        else:
            print("Element not found")

    elif choice == 21:
        num = int(input("Enter number: "))
        print("Occurrences =", list1.count(num))

    elif choice == 22:
        num = int(input("Enter number: "))
        for i in range(len(list1)):
            if list1[i] == num:
                print("Found at position:", i)
                break
        else:
            print("Not found.")

    elif choice == 23:
        other_list = list(map(int, input("Enter another list: ").split()))
        common = [x for x in list1 if x in other_list]
        print("Common elements:", common)

    elif choice == 24:
        list1.reverse()
        print("Reversed list:", list1)

    elif choice == 25:
        print("New sorted list:", sorted(list1))

    elif choice == 26:
        order = input("Enter 'asc' or 'desc': ").strip().lower()
        if order not in ("asc", "desc"):
            print("Invalid choice")
            continue
        else:
            if order == "asc":
                list1.sort()
            else:
                list1.sort(reverse=True)
        print("Sorted list:", list1)

    elif choice == 27:
        print("Total number of elements =", len(list1))

    elif choice == 28:
        if list1:
            print("Max element =", max(list1))
        else:
            print("List is empty")

    elif choice == 29:
        if list1:
            print("Min element =", min(list1))
        else:
            print("List is empty")

    elif choice == 30:
        if list1:
            print("Sum =", sum(list1))
        else:
            print("List is empty")

    elif choice == 31:
        uniq = sorted(dict.fromkeys(list1), reverse=True)
        if len(uniq) >= 3:
            print("Largest =", uniq[0])
            print("Second largest =", uniq[1])
            print("Third largest =", uniq[2])
        else:
            print("Not enough unique elements.")

    elif choice == 32:
        list2 = list(map(int, input("Enter the second list to compare with: ").split()))
        if list1 == list2:
            print("The lists are identical.")
        else:
            print("The lists are different.")

    elif choice == 33:
        print("The list is: ", list1)

    else:
        print("Enter a valid number (from 0 to 33)")
        continue