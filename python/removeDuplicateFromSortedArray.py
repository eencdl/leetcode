__author__ = 'don'
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
 It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return nums

        p = 1
        for i in range(2, len(nums)):
            if nums[p] != nums[p-1]:
                p += 1
            nums[p] = nums[i]
        return nums

if __name__ == '__main__':
    print Solution().removeDuplicates([1])
