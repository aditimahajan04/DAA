def partition(array, low, high):
    # Select the first element as the pivot
    pivot = array[low]
    i = low + 1  # Initialize index for the smaller element

    # Traverse through the array and rearrange elements based on pivot
    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]  # Swap if element is smaller than pivot
            i += 1  # Move to the next position for the smaller element

    # Swap the pivot element to its correct position
    array[low], array[i - 1] = array[i - 1], array[low]

    # Return the index of the pivot element after partitioning
    return i - 1


def quicksort(array, low, high):
    # Recursive QuickSort function
    if low < high:
        # Partition the array and get the index of the pivot
        pi = partition(array, low, high)

        # Recursively apply QuickSort to the sub-arrays
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


if __name__ == '__main__':
    # Read the number of elements from the user
    n = int(input("Enter the number of elements: "))

    # Read the array elements from the user
    array = list(map(int, input("Enter the elements separated by spaces: ").split()))

    # Ensure that the number of elements entered matches the specified size
    if len(array) != n:
        print("The number of elements entered does not match the specified size.")
    else:
        # Apply QuickSort to the array
        quicksort(array, 0, n - 1)

        # Print the sorted array
        print("Sorted array:", array)

#Time Complexity: O(nlogn)
#Space Complexity: O(logn)
