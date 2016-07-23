__author__ = 'don'
"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for n in nums:
            xor ^= n

        # XOR will have at least 1 bit is 1 since the 2 numbers are different
        mask = 1
        while xor & mask == 0:
            mask = mask << 1

        # Find that 1 bit diff to split the number list to 2 lists
        # and then XOR each list
        xor1 = 0
        xor2 = 0
        for n in nums:
            if n & mask == 0:
                xor1 ^= n
            else:
                xor2 ^= n

        return [xor1, xor2]

