__author__ = 'don'
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # (ab) mod c == ((a mod c) (b mod c)) mod c
        # (a pow(mn)) mod c == (a pow(m) mod c) (a pow(n) mod c) mod c
        r, p = 1, a
        for i in b[::-1]:
            r = (r * (p ** i) % 1337) % 1337
            p = (p ** 10) % 1337


print(Solution().superPow(2,[3]))