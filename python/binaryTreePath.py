__author__ = 'don'
"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        lst = []
        def helper(node, s):
            if node is None:
                return
            ts = s + '->' + str(node.val)
            if node.left is None and node.right is None:
                lst.append(ts)
            else:
                helper(node.left, ts)
                helper(node.right, ts)
            return

        if root is None:
            return lst
        else:
            ss = str(root.val)
            if root.left is None and root.right is None:
                lst = [str(root.val)]
            else:
                if root.left:
                    helper(root.left, ss)
                if root.right:
                    helper(root.right, ss)

        return lst

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(8)
    print Solution().binaryTreePaths(root)




