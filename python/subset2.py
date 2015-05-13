__author__ = 'don'
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        # use DFS
        def dfs(depth, s, r):
            #append at every entry
            if r not in res:
                res.append(r)
            if depth == len(nums):
                return

            for i in range(s, len(nums)):
                dfs(depth+1, i+1, r + [nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])
        return res
