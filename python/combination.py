__author__ = 'don'
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def __init__(self):
        self.result = []

    def combine(self, n, k):
        self.helper(n,k,0,[])
        return self.result




    def helper(self, n, k, s, r):
        if len(r) == k:
            nl = r[:]
            self.result.append(nl)
            return

        for i in range(s, n):
            self.helper(n, k, s+1, r+i)


