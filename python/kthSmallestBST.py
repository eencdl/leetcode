# -*- coding: utf-8 -*-
__author__ = 'don'

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?



"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = 0
        self.cnt = 0
        self.val = 0
        def getK(node):

            if node.left:
                getK(node.left)

            self.cnt += 1
            if self.cnt == k:
                self.val = node.val
                return

            if node.right:
                getK(node.right)

        getK(root)
        return self.val

root = TreeNode(1)
root.right = TreeNode(2)
print Solution().kthSmallest(root, 2)