__author__ = 'don'
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        result=''
        while n > 0:
            result = chr(ord('A') + (n-1) % 26) + result
            n = (n-1)/26
        return result
