__author__ = 'don'
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        #collect most max and most min
        if len(nums) == 0:
            return 0

        res = nums[0]
        minp = nums[0]
        maxp = nums[0]
        for a in nums[1:]:
            tmp_maxp = maxp
            tmp_minp = minp
            maxp = max(max(tmp_maxp*a, tmp_minp*a), a)
            minp = min(min(tmp_maxp*a, tmp_minp*a), a)
            res = max(res, maxp)
        return res

if __name__ == '__main__':
    print Solution().maxProduct([2, -5, -2, -4, 3])