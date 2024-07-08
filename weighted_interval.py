def weighted_interval_scheduling(intervals):
    # Sort intervals by finish time to ensure we are considering intervals in order of their end times
    intervals.sort(key=lambda x: x[1])  # x[1] is the finish time

    memo = {}  # Dictionary to store results of subproblems for memoization

    def recurse(index):
        if index < 0:  # Base case: no intervals left to consider
            return 0

        if index in memo:  # If result for this index is already computed, return it
            return memo[index]

        # Find the latest non-overlapping interval before the current one
        latest_non_overlap = -1
        for i in range(index - 1, -1, -1):  # Iterate from current index - 1 down to 0
            if intervals[i][1] <= intervals[index][0]:  # If finish time of interval i is less than or equal to start time of current interval
                latest_non_overlap = i
                break  # Found the latest non-overlapping interval, exit the loop

        # Calculate maximum weight by either including or excluding the current interval
        include = intervals[index][2]  # Value of the current interval
        if latest_non_overlap != -1:  # If there is a non-overlapping interval
            include += recurse(latest_non_overlap)  # Add the result of the subproblem including the latest non-overlapping interval

        exclude = recurse(index - 1)  # Calculate the result of the subproblem excluding the current interval

        # Memoize the result for the current index
        memo[index] = max(include, exclude)  # Maximum value by either including or excluding the current interval

        return memo[index]  # Return the result for the current index

    return recurse(len(intervals) - 1)  # Start the recursion from the last interval

# Example usage with the given table values:
intervals = [
    (1, 2, 100),  # Interval 1 with start time 1, finish time 2, and value 100
    (2, 5, 200),  # Interval 2 with start time 2, finish time 5, and value 200
    (3, 6, 300),  # Interval 3 with start time 3, finish time 6, and value 300
    (4, 8, 400),  # Interval 4 with start time 4, finish time 8, and value 400
    (5, 9, 500),  # Interval 5 with start time 5, finish time 9, and value 500
    (6, 10, 100)  # Interval 6 with start time 6, finish time 10, and value 100
]
print("Maximum profit:", weighted_interval_scheduling(intervals))  # Print the maximum profit



#Time complexity:O(n^2)
#Space complexity:O(n)
