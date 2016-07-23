__author__ = 'don'
"""
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) = 1
sumRange(2, 5) = -1
sumRange(0, 5) = -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.c = []
        for n in nums:
            print self.c
            if len(self.c) > 0:
                self.c.append(n+self.c[-1])
            else:
                self.c.append(n)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.c:
            return self.c[j] if i == 0 else self.c[j] - self.c[i-1]
        return 0

if __name__ == '__main__':
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print n.sumRange(0, 2)
    print n.sumRange(2, 5)
    print n.sumRange(0, 5)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
