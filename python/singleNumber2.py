__author__ = 'don'
"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one = 0
        two = 0
        for i in range(len(nums)):
            # retain appear twice
            two |= nums[i] & one

            # the usual single occurence
            one ^= nums[i]

            # only if it happen 3 times, t will have its values
            t = one & two

            # clear 3 times for one & two
            one &= ~t
            two &= ~t
        return one


if __name__ == '__main__':
    print Solution().singleNumber([2, 5, 2, 3, 5, 5, 2])

