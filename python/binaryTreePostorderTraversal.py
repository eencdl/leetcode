__author__ = 'don'
"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

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
    def postorderTraversal(self, root):
        r = []
        self.helper(root, r)
        return r

    def helper(self, root, r):
        if root is None:
            return
        self.helper(root.left, r)
        self.helper(root.right, r)
        r.append(root.val)


