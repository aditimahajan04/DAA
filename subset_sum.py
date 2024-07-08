def can_form_subset(arr, target):
    def check_subset(arr, target, index):
        # Base case: if the target is 0, a subset with the required sum is found
        if target == 0:
            return True

        # Base case: if no more elements are left to check, return False
        if index >= len(arr):
            return False

        # Include the current element in the subset and check if the target can be met
        include = check_subset(arr, target - arr[index], index + 1)

        # Exclude the current element from the subset and check if the target can be met
        exclude = check_subset(arr, target, index + 1)

        # Return True if either including or excluding the current element meets the target
        return include or exclude

    # Start the recursion from the first element
    return check_subset(arr, target, 0)


# Example usage with the given array and target sum:
arr = [3, 34, 4, 12, 5, 2]
target = 9

if can_form_subset(arr, target):
    print(f"Yes, there is a way to pick some numbers from {arr} that add up to {target}.")
else:
    print(f"No, it's not possible to pick some numbers from {arr} that add up to {target}.")


#Time complexity:O(2^n)
#Space complexity:O(n)
