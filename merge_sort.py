def merge(arr, l, m, r):
    # Calculate the sizes of the two subarrays to be merged
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays to hold the values of the left and right subarrays
    L = [0] * n1
    R = [0] * n2

    # Copy the data to the temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Initial indices for L[], R[], and the merged array
    i = 0  # Initial index of the first subarray
    j = 0  # Initial index of the second subarray
    k = l  # Initial index of the merged array

    # Merge the temporary arrays back into arr[l..r]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    # Only proceed if the array has more than one element
    if l < r:
        # Find the middle point to divide the array into two halves
        m = l + (r - l) // 2

        # Recursively sort the first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # Merge the two halves sorted above
        merge(arr, l, m, r)


if __name__ == '__main__':
    # Read the size of the array from the user
    n = int(input("Enter the number of elements in the array: "))

    # Read the array elements from the user
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    # Ensure that the number of elements entered matches the specified size
    if len(arr) != n:
        print("The number of elements entered does not match the specified size.")
    else:
        # Call the mergeSort function to sort the array
        mergeSort(arr, 0, n - 1)

        # Print the sorted array
        print("Sorted array:", arr)


#Time Complexity: O(nlogn)
#Space Complexity: O(n)
