def can_form_subset(arr, target):
    def check_subset(arr, target, index):
        if target == 0:
            return True
        if index >= len(arr):
            return False

        include = check_subset(arr, target - arr[index], index + 1)
        exclude = check_subset(arr, target, index + 1)

        return include or exclude

    return check_subset(arr, target, 0)


if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter the elements separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))

    if can_form_subset(arr, target):
        print("Yes")
    else:
        print("No")

#Time Complexity:O(2^n)
#Space Complexity:O(n)
