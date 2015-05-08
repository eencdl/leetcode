__author__ = 'don'

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        y = abs(x)
        r = 0
        while y > 0:
            r = r*10 + (y%10)
            y /= 10
        if x < 0:
            return -1 * r
        else:
            return r



