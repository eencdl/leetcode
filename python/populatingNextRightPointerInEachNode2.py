__author__ = 'don'
"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #using BFS
        if root is None:
            return

        cnt, level, q = 0, 1, [root]
        while len(q) > 0:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
                cnt += 1
            if node.right is not None:
                q.append(node.right)
                cnt += 1
            level -= 1
            if level == 0:
                node.next = None
                level, cnt = cnt, 0
            else:
                node.next = q[0]
        return
