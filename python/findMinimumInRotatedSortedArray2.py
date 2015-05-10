__author__ = 'don'
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.



Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        return self.helper(nums, 0, len(nums)-1)


    def helper(self, nums, s, e):
        if e-s <= 1:
            return min(nums[s], nums[e])
        mid = (s+e)/2

        if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
            return nums[mid]
        elif nums[mid] > nums[e]:
            return self.helper(nums, mid+1, e)
        else:
            return self.helper(nums, s, mid-1)




