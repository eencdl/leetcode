__author__ = 'don'
"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    # The goal here is that 5x2 pairs form a zero
    # 2 is more occurences than 5, so we only need to count 5
    def trailingZeroes(self, n):
        cnt = 0
        k = 5
        while n >= k:
            cnt += n/k
            k *= 5
        return cnt