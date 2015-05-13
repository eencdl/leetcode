__author__ = 'don'
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}"
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        # using the array smartly as a queue and stack
        # when insert at front, pop from back
        # when append at back, pop from the front
        # append back (left, then right), when pop at front
        # insert front (right, then left), when pop at back
        # in both cases: you want to the queue = [left right left right left right]
        # so that if  you want the reverse just pop from back, or pop from front to get normal order
        def bfs(root):
            if root is None:
                return []
            r, cnt, level, q, res = False, 0, 1, [root], []
            while len(q) > 0:
                if r:
                    node = q.pop()
                    if node.right:
                        cnt += 1
                        q.insert(0, node.right)
                    if node.left:
                        cnt += 1
                        q.insert(0,node.left)

                else:
                    node = q.pop(0)
                    if node.left:
                        cnt += 1
                        q.append(node.left)
                    if node.right:
                        cnt += 1
                        q.append(node.right)

                level -= 1
                res.append(node.val)
                if level == 0:
                    level, cnt = cnt, 0
                    r = ~r
                    tres.append(res[:])
                    res = []

        tres =[]
        bfs(root)
        return tres
