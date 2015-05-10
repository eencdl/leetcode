__author__ = 'don'
"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        r = []
        self.helper(root, r)
        return r

    def helper(self, root, r):
        if root is None:
            return
        r.append(root.val)
        self.helper(root.left, r)
        self.helper(root.right, r)

