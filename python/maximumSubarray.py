__author__ = 'don'
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        msum = float('-inf');
        rsum = 0

        for i in nums:
            rsum += i
            msum = max(msum, rsum)
            if rsum < 0:
                rsum = 0
        return msum
