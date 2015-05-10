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
    # use 1,2,3,4,5 to see what condition to binary search
    # remove half every time
    # 1,2,2,2,5
    # 5,1,2,2,2
    # 2,5,1,2,2
    # 2,2,5,1,2
    # 2,2,2,5,1
    # You can see always keep the right half (inclusive) 
    # if mid is greater or equal to left, and greater than right
    # SPECIAL CASE we had to explore both branch, when all left, mid, right has the same values
    # 1,2,2,2,2
    # 2,1,2,2,2 (undecided)
    # 2,2,1,2,2
    # 2,2,2,1,2 (undecided)
    # 2,2,2,2,1
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




