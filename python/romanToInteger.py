__author__ = 'don'
"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
I, II, III, IV, V, VI, VII, VIII, IX, X
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        # the cleanest way CM（M-C=1000-100=900）
        # is to do C + M - 2*C = 900
        d = {'I': 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M':1000 }
        last = None
        sum = 0
        for i in s:
            num = d[i]
            if last and num > last:
                sum -= 2*last
            sum += num
            last = num
        return sum
