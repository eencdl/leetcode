__author__ = 'don'
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(1) = 10
        # f(2) = 9*9 + f(1) = 91 (9x9 because 1st digit has 9 possibilities excluding 0, 2nd digit has 9 possibilities after 1 digit
        # f(3) = 9*9*8 + f(2) + f(1)
        # f(n) = 9* (9 choose n-1) + f(n-1) + ... + f(1)
        l = [1, 9]

        for i in xrange(9, 0, -1):
            l += [l[-1]*i]
        return sum(l[:n+1])

print(Solution().countNumbersWithUniqueDigits(4))
