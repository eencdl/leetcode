__author__ = 'don'
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        if root is None:
            return True
        return self.helper(root.left, float("-inf"), root.val) and self.helper(root.right, root.val, float("inf"))

    def helper(self, root, lf, rg):
        if root is None:
            return True

        if root.val > lf and root.val < rg:
            return self.helper(root.left, lf, root.val) and self.helper(root.right, root.val, rg)

        return False


