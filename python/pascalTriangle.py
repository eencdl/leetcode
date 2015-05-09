__author__ = 'don'
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numrow):
        if numrow == 0:
            return []

        return self.getList(numrow, [[1]])

    def getList(self, n, arr):
        if n <= 1:
            return arr
        r = [1]
        for i in range(1, len(arr[-1])):
            r.append(arr[-1][i - 1] + arr[-1][i])
        r.append(1)
        arr.append(r)
        return self.getList(n - 1, arr)


if __name__ == '__main__':
    print Solution().generate(3)
