__author__ = 'don'
"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        p1 = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p1] = nums[i]
                p1 += 1
        return nums

if __name__ == "__main__":
    print Solution().removeElement([1],1)