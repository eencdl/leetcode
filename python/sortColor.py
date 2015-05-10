__author__ = 'don'
"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        f, m, e = 0, 0, len(nums)-1
        while m < e:
            if nums[f] == 0:
                f += 1

            if nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[m] = nums[e]
                nums[e] = 2
            else:
                nums[m] = nums[f]
                nums[f] = 0

            if nums[e] == 2:
                e -= 1