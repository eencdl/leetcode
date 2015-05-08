__author__ = 'don'
"""
Description:

Count the number of prime numbers less than a non-negative number, n
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 2:
            return 0

        l = [True]*n
        l[0] = False
        l[1] = False
        i = 2
        while i*i < n:
            if l[i]:
                j=i+i
                while j < n:
                    l[j] = False
                    j += i
            i += 1

        t = 2
        cnt = 0
        while t < n:
            if l[t]:
                cnt +=1
            t += 1

        return cnt