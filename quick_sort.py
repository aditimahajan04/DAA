def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

array = [9, 5, 4, 0, 1, 6]
n = len(array)
quicksort(array, 0, n - 1)
print(array)
