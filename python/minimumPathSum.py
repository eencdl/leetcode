__author__ = 'don'
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        # Must use DP, greedy won't work
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # another way is to populate dp[0][:] and dp[:][0] with float('inf')
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if j-1 < 0 and i-1 < 0:
                    dp[i][j] = grid[i][j]
                elif j-1 < 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i-1 < 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]

if __name__ == '__main__':
    print Solution().minPathSum([[1, 2],[1,1]])