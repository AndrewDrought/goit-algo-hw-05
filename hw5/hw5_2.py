def binary_search(array, value):
    low = 0
    high = len(array) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return iterations, array[mid]
        iterations += 1

    return iterations, array[low] if low < len(array) else None

arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
print(binary_search(arr, 3.5))