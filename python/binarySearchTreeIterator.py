__author__ = 'don'
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node
of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        if root:
            self.stack.append(root)
            while root.left is not None:
                self.stack.append(root.left)
                root = root.left


    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0


    # @return an integer, the next smallest number
    def next(self):
        node = self.stack[-1]
        self.stack.pop()
        if node.right:
            r = node.right
            self.stack.append(r)
            while r.left is not None:
                self.stack.append(r.left)
                r = r.left
        return node.val



