#!/usr/bin/python3
"""Solves the challenge of:
placing N non-attacking queens on an N×N chessboard
"""

import sys


def is_safe(board, row, col, n):
    """Checks for correct parameters"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(n):
    """Solves the N queens problem"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(board, col):
        if col == n:
            solution = []
            for row in board:
                solution.append("".join(["Q" if x == 1 else "." for x in row]))
            solutions.append(solution)
            return
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    solve(board, 0)
    return solutions

def main():
    """Main method"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    main()
