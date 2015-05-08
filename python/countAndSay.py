__author__ = 'don'
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        return self.helper(n,'1')

    def helper(self, n, seq):
        if n == 1:
            return seq

        newSeq = ''
        base = seq[0]
        cnt = 1
        for i in range(1, len(seq)):
            if base == seq[i]:
                cnt += 1
            else:
                newSeq += str(cnt) + base
                cnt = 1
                base = seq[i]
        newSeq += str(cnt) + base
        return self.helper(n-1, newSeq)





