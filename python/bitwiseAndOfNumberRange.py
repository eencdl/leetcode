__author__ = 'don'
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        cnt = 0 #number of shift back needed

        #keep shifting right until equal
        while m != n and m > 0:
            n >>= 1
            m >>= 1
            cnt += 1
        return m << cnt