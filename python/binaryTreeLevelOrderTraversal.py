__author__ = 'don'
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        r = []
        if root is None:
            return r

        cnt, level, r, r1 = 0, 1, [], []
        q = [root]
        while len(q) > 0:
            node = q.pop(0)

            if node.left is not None:
                cnt += 1
                q.append(node.left)
            if node.right is not None:
                cnt += 1
                q.append(node.right)

            level -= 1
            r1.append(node.val)
            if level == 0:
                r.append(r1)
                level, cnt, r1 = cnt, 0, []
        return r


