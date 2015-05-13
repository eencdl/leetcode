__author__ = 'don'
"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        # use DFS
        def dfs(depth, s, r):
            #append at every entry
            res.append(r)
            if depth == len(nums):
                return

            for i in range(s, len(nums)):
                dfs(depth+1, i+1, r + [nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])
        return res

if __name__ == '__main__':
    print Solution().subsets([1,2,3])
