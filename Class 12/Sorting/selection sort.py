def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:  # avoid unnecessary swap
            arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [8, 7, 13, 1, -9, 4]
selection_sort(arr)

print("The sorted list is:", *arr)