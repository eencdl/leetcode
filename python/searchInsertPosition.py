__author__ = 'don'
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
[1,3,5,6], 5 => 2
[1,3,5,6], 2 => 1
[1,3,5,6], 7 => 4
[1,3,5,6], 0 => 0
You may assume no duplicates in the array.

Here are few examples.

"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        return self.helper(nums, 0, len(nums)-1, target)


    def helper(self, nums, s, e, target):
        if (e-s) <= 1:
            if target <= nums[s]:
                return s
            elif target > nums[e]:
                return e+1
            else:
                return e

        mid = (s+e)/2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.helper(nums, mid, e, target)
        else:
            return self.helper(nums, s, mid, target)

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5], 2)
