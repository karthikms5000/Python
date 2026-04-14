def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # stop early if already sorted
            break

arr = [8, 7, 13, 1, -9, 4]
bubble_sort(arr)

print("The sorted list is:", *arr)