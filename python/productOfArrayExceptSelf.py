__author__ = 'don'
"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

Solutions:

     num [ 1  2  3  4]
    left [    1  2  6]
    right[24 12  4   ]
    result = left * right = [24 12 8 6]
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls = 1
        rs = 1
        l = 0
        n = len(nums)
        results = [1] * n
        r = n - 1
        for l in range(0,r):
            ls *= nums[l]
            results[l+1] *= ls
            rs *= nums[r]
            results[r-1] *= rs
            r -= 1
        return results