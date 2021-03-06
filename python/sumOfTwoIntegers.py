__author__ = 'don'
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # a ^ b is the summation without the carry
        # a & b is the carry that is right shifted
        # keep right shifting since there might be new carry
        # generated by the previous carry
        # lastly, if it is negative number use 2's compliment ~a+1
        # since we cannot use +, ~ (a & MAX_INT) ^ MAX_INT
        MOD=0xFFFFFFFF
        MAX_INT=0x7FFFFFFF
        while b != 0:
            a, b = (a^b) & MOD, ((a&b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT
