__author__ = 'don'
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
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
    # @param {integer} sum
    # @return {integer[][]}
    class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def __init__(self):
        self.result = []

    def pathSum(self, root, sum):
        if root == None or root == []:
            return []
        self.helper(root, root.val, sum, [root.val])
        return self.result

    def helper(self,root, csum, sum, r):

        if csum == sum and root.left is None and root.right is None:
            self.result.append(r)
            return

        if root.left is not None:
            self.helper(root.left, csum+root.left.val, sum, r + [root.left.val])
        if root.right is not None:
            self.helper(root.right, csum+root.right.val, sum, r + [root.right.val])


        if root.left:
            self.helper(root.left, csum+root.left.val, sum, r + [root.left.val])
        if root.right:
            self.helper(root.right, csum+root.right.val, sum, r + [root.right.val])

if __name__ == "__main__":
    print Solution().pathSum([],1)
