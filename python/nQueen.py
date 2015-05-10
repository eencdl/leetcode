__author__ = 'don'
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution:
    # @return a list of lists of string
    # use matrix system, the array key is row, the value is col
    def solveNQueens(self, n):
        def check(x, y):
            for i in range(x):
                if (board[i]) == y or (abs(x-i) == abs(y-board[i])):
                    return False
            return True

        def dfs(depth, result):
            if depth == n:
                r.append(result)

            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth+1, result+ [s[:i] + 'Q' + s[i+1:]])

        board = [-1 for j in range(n)]
        r = []
        dfs(0, [])
        return r