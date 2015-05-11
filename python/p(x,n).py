__author__ = 'don'
"""
Implement pow(x, n).
"""
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        # The KEY POINT is n%2 == 1, store the current multiplier
        # let x keep squaring, x2, x4, x8 ...., every time we squared we divide n by 2
        # only when n%2 == 1, we pick up the multiplier
        # remember if you keep divide by 2, eventually you will get 1, which pick up
        # the last multiplier
        if x == 0:
            return 0
        if n == 0:
            return 1

        ntive = False
        if n < 0:
            n = abs(n)
            ntive = True

        res = 1
        while n > 0:
            #pick up the multiplier when
            #n mod 2 is 1
            if (n%2) == 1:
                res *= x

            x *= x
            n /= 2
        if ntive:
            return 1/res
        else:
            return res
