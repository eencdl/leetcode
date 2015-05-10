__author__ = 'don'
"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # backtracking
    def __init__(self):
        self.result = []

    def permute(self, nums):
        self.helper(nums, 0)
        return self.result



    def helper(self, nums, s):
        if s == len(nums):
            nlist = nums[:]
            self.result.append(nlist)
            return

        for i in range(s, len(nums)):
            self.swap(nums, s, i)
            self.helper(nums, s+1)
            self.swap(nums, s, i)

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

if __name__ == '__main__':
    print Solution().permute([1, 2, 3])