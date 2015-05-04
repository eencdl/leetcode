__author__ = 'don'
class Solution:
    def rangeBitwiseAnd(self,m,n):
        #just need to find the common most left bits
        cnt = 0 #number of shift back needed

        #keep shifting right until equal
        while m != n and m > 0:
            n >>= 1
            m >>= 1
            cnt += 1


        return m << cnt
