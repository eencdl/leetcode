__author__ = 'don'
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        return self.getList(rowIndex,[1])

    def getList(self, n, arr):
        if n <= 0:
            return arr
        r = [1]
        for i in range(1, len(arr)):
            r.append(arr[i-1] + arr[i])
        r.append(1)
        return self.getList(n-1, r)
