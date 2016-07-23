__author__ = 'don'
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the key is 3, extract as much 3 as possible
        # 3 => 2 + 1 = 2
        # 4 => 2 + 2 = 4
        # 5 => 2 + 3 = 6
        # 6 => 3 + 3 = 9
        # 7 => 3 + 4 = 12
        # 8 => 3 + 3 + 2 = 18
        # 9 => 3 + 3 + 3 = 27
        # 10 => 3 + 3 + 4 = 36
        dp = [0, 0, 1, 2, 4, 6, 9]
        for i in xrange(7, n+1):
            dp.append(3 * dp[i-3])
        return dp[n]
print(Solution().integerBreak(2))
print(Solution().integerBreak(4))
print(Solution().integerBreak(10))
#print(Solution().integerBreak(23))


