__author__ = 'don'
"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        # use binary search
        # we know that x = sqrt(x) * sqrt(x)
        # this is assuming the sqrt is going to be an integer

        if x == 0:
            return 0
        i = 1
        j = x / 2 + 1
        while i <= j:
            mid = (i + j) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                j = mid - 1
            else:
                i = mid + 1

        return j


if __name__ == '__main__':
    print Solution().mySqrt(2)
