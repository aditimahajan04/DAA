def knapsack(items, i, curr_weight, w, dp):
    # Base case: If all items have been considered
    if i >= len(items):
        return 0

    # Return already computed result if it exists
    if dp[i][curr_weight] != -1:
        return dp[i][curr_weight]

    # Case 1: Include the current item if it fits in the knapsack
    case1 = 0
    if curr_weight + items[i][1] <= w:
        case1 = items[i][2] + knapsack(items, i + 1, curr_weight + items[i][1], w, dp)

    # Case 2: Exclude the current item
    case2 = knapsack(items, i + 1, curr_weight, w, dp)

    # Store the result in dp array and return it
    dp[i][curr_weight] = max(case1, case2)
    return dp[i][curr_weight]


if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []

    for _ in range(n):
        item_id, weight, value = map(int, input("Enter item id, weight, and value separated by spaces: ").split())
        items.append((item_id, weight, value))

    w = int(input("Enter the maximum weight capacity of the knapsack: "))

    # Initialize the dp array with -1 to indicate that no subproblem has been solved yet
    dp = [[-1 for _ in range(w + 1)] for _ in range(len(items))]

    # Call the knapsack function and print the result
    print("Maximum value in knapsack:", knapsack(items, 0, 0, w, dp))
# Time Complexity:O(n*w)
# Space Complexity:O(n*w)
