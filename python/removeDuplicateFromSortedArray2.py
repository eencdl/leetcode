__author__ = 'don'
"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1

        cnt = 0
        p = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 0

            if cnt < 2:
                p += 1

            nums[p] = nums[i]

        return p+1

if __name__ == '__main__':
    print Solution().removeDuplicates([1,1,1,2,2,2,3,3,3,3,3])
