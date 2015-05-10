__author__ = 'don'
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    # f(n) = f(n-1) + f(n-2)
    # must use dp to save time
    # fibonacci seq
    def climbStairs(self, n):
        dp = [1]*(n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1]+ dp[i-2]
        return dp[n]
