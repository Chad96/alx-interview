#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""

import sys


def generate_solutions(n):
    """Generate all possible solutions for n queens on an n x n board"""
    solutions = [[]]
    for queen in range(n):
        solutions = place_queen(queen, n, solutions)
    return solutions


def place_queen(queen, n, prev_solutions):
    """Place a queen in a valid position"""
    safe_positions = []
    for solution in prev_solutions:
        for col in range(n):
            if is_safe(queen, col, solution):
                safe_positions.append(solution + [col])
    return safe_positions


def is_safe(row, col, solution):
    """Check if a position is safe for the queen"""
    for r in range(row):
        c = solution[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def init():
    """Initialize and validate command-line arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """Solve the N Queens problem and print all solutions"""
    n = init()
    solutions = generate_solutions(n)
    for solution in solutions:
        result = []
        for row, col in enumerate(solution):
            result.append([row, col])
        print(result)


if __name__ == '__main__':
    n_queens()
