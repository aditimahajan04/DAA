def solve_n_queens(n):
    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen at board[row][col].
        """
        for i in range(row):
            # Check column and diagonals
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        """
        Solve the N-Queens problem using backtracking.
        """
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                # Backtrack
                board[row] = -1

    def print_solution(solution):
        """
        Print a single solution in a readable format.
        """
        for i in range(n):
            row = ['.'] * n
            row[solution[i]] = 'Q'
            print(" ".join(row))
        print("\n")

    result = []
    solve([-1] * n, 0)

    # Print all solutions
    for solution in result:
        print_solution(solution)

    return result

if __name__ == "__main__":
    # Input the size of the chessboard
    n = int(input("Enter the size of the chessboard (n): "))

    # Ensure n is a positive integer
    if n <= 0:
        print("The size of the chessboard must be a positive integer.")
    else:
        solutions = solve_n_queens(n)
        print(f"Total solutions: {len(solutions)}")
# Time Complexity:O(N!)
# Space Complexity:O(N^2)
