def knapsack(items, i, curr_weight, weight, dp):
    # Base case: If we have considered all items, return 0 (no more value to add).
    if i >= len(items):
        return 0

    # If the value for current item and current weight combination is already computed, return it.
    if dp[i][curr_weight] != -1:
        return dp[i][curr_weight]

    # Case 1: Include the current item if its weight can be accommodated within the remaining capacity.
    case1 = 0
    if curr_weight + items[i][1] <= weight:
        # Recursively calculate the value if including the current item.
        case1 = items[i][2] + knapsack(items, i + 1, curr_weight + items[i][1], weight, dp)

    # Case 2: Exclude the current item and move to the next item.
    case2 = knapsack(items, i + 1, curr_weight, weight, dp)

    # Choose the maximum value between including and excluding the current item.
    dp[i][curr_weight] = max(case1, case2)

    # Return the maximum value that can be obtained for the current state.
    return dp[i][curr_weight]


if __name__ == "__main__":
    # Test case with given items and maximum weight capacity.
    items = [(1, 3, 10), (2, 5, 4), (3, 6, 9), (4, 2, 11)]
    w = 7

    # Initialize a DP table with -1 indicating that no values have been computed yet.
    dp = [[-1 for _ in range(w + 1)] for _ in range(len(items))]

    # Call the knapsack function with initial parameters and print the result.
    print("Maximum value that can be accommodated in the backpack is:", knapsack(items, 0, 0, w, dp))

#Time complexity:O(n*w)
#Space complexity:O(n*w)
