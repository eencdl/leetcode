__author__ = 'don'
"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        r = []
        def helper(h, p):
            if h == p:
                r.append(str(h))
            else:
                r.append(str(h) + '->' + str(p))

        if not nums:
            return nums
        h = p = None

        for n in nums:
            if h is None:
                h = n
            elif n-p != 1:
                helper(h, p)
                h = n
            p = n
        helper(h, p)

        return r