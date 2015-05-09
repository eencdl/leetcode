__author__ = 'don'
"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        if len(s) == 0:
            return 0
        r = 0
        for i in s:
            r *= 26
            r += (ord(i) - ord('A') + 1)

        return r

if __name__ == "__main__":
    print Solution().titleToNumber('ZZ')