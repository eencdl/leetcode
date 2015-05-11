__author__ = 'don'
"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""
class Solution:
    # @param nums, an integer[]
    # @return an integer
    # remember both ends are -inf
    def findPeakElement(self, nums):
        if len(nums) == 0:
            return -1
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, s, e):
        if s == e:
            return s

        if (e-s) == 1:
            return [s, e][nums[s] < nums[e]]

        mid = (s+e)/2
        #upslope
        if nums[mid] > nums[mid-1]:
            return self.helper(nums, mid, e)
        else:
            return self.helper(nums, s, mid)
