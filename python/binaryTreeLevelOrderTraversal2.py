__author__ = 'don'
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
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
    def levelOrderBottom(self, root):
        r = []
        if root is None:
            return r
        # use BFS
        q = [root]
        r1, cnt, level = [], 0, 1

        while len(q) > 0:
            node = q.pop(0)
            r1.append(node.val)
            level -= 1

            if node.left is not None:
                q.append(node.left)
                cnt += 1

            if node.right is not None:
                q.append(node.right)
                cnt += 1

            if level == 0:
                r.insert(0, r1)
                r1 = []
                level = cnt
                cnt = 0
        return r






if __name__ == "__main__":
    a = [[1],[1,2],[1,2,3]]
    print a
