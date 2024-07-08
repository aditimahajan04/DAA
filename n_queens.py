def solve_n_queens(n):
    # Function to check if placing a queen at board[row][col] is safe
    def is_safe(board, row, col):
        # Check each row above the current row
        for i in range(row):
            # Check if there's a queen in the same column or diagonals
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    # Recursive function to find all solutions starting from a given row
    def solve(board, row):
        # If all queens are placed, add the current board configuration to results
        if row == n:
            result.append(board[:])
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place queen at board[row][col]
                solve(board, row + 1)  # Recur to place queen in the next row
                board[row] = -1  # Backtrack by resetting to -1 after exploring

    # Initialize an empty list to store all solutions
    result = []
    # Start solving from the first row with an empty board
    solve([-1] * n, 0)
    return result

# Example usage:
n = 4
solutions = solve_n_queens(n)
print("Number of solutions:", len(solutions))
for solution in solutions:
    print(solution)
