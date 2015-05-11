__author__ = 'don'
"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
Denote bst[i] = the number of BSTs can be constructed that store values from 1..n.

n = 1,  Node = {1},      bst[1]  = 1

n = 2,  Node = {1, 2}
when 1 is the root node, there is 1 bst
   1
    \
    2
when 2 is the root node, there is 1 bst
   2
  /
1
bst[2] = 2

n = 3,  Node = {1, 2, 3}
when 1 is the root node, bst[3] =  bst[3] + bst[2] where stores 2 values (2 and 3)
1                                                   1                   1
 \                                 =                 \                    \
 BSTs of {2,3}                              2                    3
                                                       \                   /
                                                        3                2
when 2 is the root node, bst[3] =  bst[3] + bst[1] + bst[1]
          2
         /  \
        1   3
when 3 is the root node, bst[3] =  bst[3] + bst[2] where stores 2 values (1 and 2)
                   3                                 3                   3
                /                 =                 /                    /
 BSTs of {1,2}                            2                   1
                                                   /                       \
                                                 1                         2
"""


class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n <= 1:
            return 1

        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        i = 2
        while i <= n:
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
            i += 1
        return dp[n]
