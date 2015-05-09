__author__ = 'don'
"""
Determine whether an integer is a palindrome. Do this without extra space.

"""
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = abs(x)
        t = x
        m = 1
        while t/(10*m) > 0:
            m *= 10

        n = 1

        while m > n:
            l = x/m % 10
            r = x/n % 10
            if l != r:
                return False
            m /= 10
            n *= 10
        return True



