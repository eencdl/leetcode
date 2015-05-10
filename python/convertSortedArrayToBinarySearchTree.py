__author__ = 'don'
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, s, e):
        if s > e:
            return None

        mid = (s+e)/2
        root = TreeNode(nums[mid])

        root.left = self.helper(nums, s, mid-1)
        root.right = self.helper(nums, mid+1, e)

        return root