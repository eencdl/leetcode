__author__ = 'don'
"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""


class Solution:
    # @param {integer} n
    # @return {integer}
    def __init__(self):
        self.cnt = 0

    def totalNQueens(self, n):
        def check(x, y):
            for i in range(x):
                if (board[i]) == y or (abs(x - i) == abs(y - board[i])):
                    return False
            return True

        def dfs(depth):
            if depth == n:
                self.cnt += 1

            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    dfs(depth + 1)

        board = [-1 for j in range(n)]
        dfs(0)
        return self.cnt