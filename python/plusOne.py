__author__ = 'don'
"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        n = len(digits)
        c = 1

        for i in range(n-1, -1, -1):
            tmp = digits[i] + c
            if tmp < 10:
                c = 0
            digits[i] = tmp % 10

        if c == 1:
            digits.insert(0,1)
        return digits





