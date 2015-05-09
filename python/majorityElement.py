__author__ = 'don'
"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            t = 0
            if d.get(i) is not None:
                t = d.get(i) + 1
            else:
                t = 1
            if t > len(nums)/2:
                    return i
            d[i] = t
        return 0


