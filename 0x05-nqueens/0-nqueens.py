#!/usr/bin/python3
""" heks for a sequence and returns a """


import sys


def solve(n, row, solution):
    if row == n:
        print(solution)
    else:
        for column in range(n):

            if all(a != column and
                   b + a != row + column and
                   b - a != row - column for b, a in solution):
                solution.append([row, column])
                solve(n, row + 1, solution)
                solution.remove([row, column])


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if isinstance(sys.argv[1], int):
        print('N must be a number')
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(int(sys.argv[1]), 0, [])
