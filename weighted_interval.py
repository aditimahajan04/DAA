def weighted_interval_scheduling(intervals):
    # Sort intervals by their finish times
    intervals.sort(key=lambda x: x[1])
    memo = {}

    def recurse(index):
        if index < 0:
            return 0
        if index in memo:
            return memo[index]

        # Find the latest non-overlapping interval
        latest_non_overlap = -1
        for i in range(index - 1, -1, -1):
            if intervals[i][1] <= intervals[index][0]:
                latest_non_overlap = i
                break

        # Calculate profit including the current interval
        include = intervals[index][2]
        if latest_non_overlap != -1:
            include += recurse(latest_non_overlap)

        # Calculate profit excluding the current interval
        exclude = recurse(index - 1)

        # Memoize and return the maximum of including or excluding the current interval
        memo[index] = max(include, exclude)
        return memo[index]

    return recurse(len(intervals) - 1)


if __name__ == "__main__":
    # Read the number of intervals
    n = int(input("Enter the number of intervals: "))

    # Read the intervals
    intervals = []
    print("Enter each interval with start time, end time, and profit (e.g., 1 2 100):")
    for _ in range(n):
        start, end, profit = map(int, input().split())
        intervals.append((start, end, profit))

    # Calculate and print the maximum profit
    max_profit = weighted_interval_scheduling(intervals)
    print("Maximum profit:", max_profit)

#Time Complexity:O(nlogn)
#Space Complexity:O(n)
