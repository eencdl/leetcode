__author__ = 'don'
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.helper(root.left, root.right)


    def helper(self, l, r):
        if l is None and r is None:
            return True
        elif l is not None and r is not None and l.val == r.val:
            return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        return False





