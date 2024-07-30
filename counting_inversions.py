def merge_and_count(arr, l, m, r):
    # Sizes of the two subarrays to be merged
    n1 = m - l + 1
    n2 = r - m

    # Temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    inversions = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            # There are (n1 - i) inversions, because all the remaining elements
            # in L[] are greater than R[j]
            inversions += (n1 - i)
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

    return inversions

def merge_sort_and_count(arr, l, r):
    inversions = 0
    if l < r:
        m = l + (r - l) // 2

        inversions += merge_sort_and_count(arr, l, m)
        inversions += merge_sort_and_count(arr, m + 1, r)
        inversions += merge_and_count(arr, l, m, r)

    return inversions

# Example usage
arr = [5, 8, 3, 9, 0, 2]
n = len(arr)
inversion_count = merge_sort_and_count(arr, 0, n - 1)
print(f"Sorted array: {arr}")
print(f"Number of inversions: {inversion_count}")
