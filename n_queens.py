def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if it's safe to place a queen at board[row][col]
        for i in range(row):
            # Check the same column
            if board[i] == col:
                return False
            # Check the diagonal
            if board[i] - i == col - row:
                return False
            # Check the anti-diagonal
            if board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        # If all queens are placed, add the solution to the result
        if row == n:
            result.append(board[:])
            return
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place the queen
                solve(board, row + 1)  # Recur to place the next queen
                # Backtrack
                board[row] = -1  # Remove the queen

    result = []
    solve([-1] * n, 0)
    return result

# Function to display the solutions on the chessboard
def print_solutions(solutions, n):
    for solution in solutions:
        for i in range(n):
            row = ['.'] * n
            row[solution[i]] = 'Q'
            print(' '.join(row))
        print("\n")

# Example usage:
n = 4
solutions = solve_n_queens(n)
print("Number of solutions:", len(solutions))
print_solutions(solutions, n)
