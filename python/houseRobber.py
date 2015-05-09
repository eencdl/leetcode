__author__ = 'don'
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is
that adjacent houses have security system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.
 """

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        # dp[i] = max(dp[i-1], dp[i-2]+num[i]
        n = len(nums)
        dp = [0] * (n+2)
        dp[0],dp[1] = 0,0
        for i in range(n):
            dp[i+2] = max(dp[i+1], dp[i]+nums[i])
        return dp[n+1]

if __name__ == '__main__':
    print Solution().rob([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])

