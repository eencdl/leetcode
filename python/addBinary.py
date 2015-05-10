__author__ = 'don'
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        m, n = len(a), len(b)

        if m > n:
            b = b.zfill(m)
        elif n > m:
            a = a.zfill(n)
        r = ''
        c = False
        for i in range(max(m-1, n-1), -1, -1):
            if a[i] == b[i]:
                if c:
                    r = '1' + r
                    if a[i] == '0':
                        c = False
                else:
                    r = '0' + r
                    if a[i] == '1':
                        c = True
            else:
                if c:
                    r = '0' + r
                else:
                    r = '1' + r

        if c:
            return '1'+ r
        else:
            return r

if __name__ == '__main__':
    print Solution().addBinary('1','111')


