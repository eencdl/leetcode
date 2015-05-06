__author__ = 'don'

"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in
the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon
entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health
(positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward
in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal
path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	 3
-5	   -10	 1
10	    30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where
the princess is imprisoned.
"""
class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        #It is a DP question, assume DP is minimum HP required
        #If dungeon < 0, then DP is 1 - dungeon  (i.e. DP > 1 since we need higher DP to survive the negative blow
        #If dungeon > 0, then DP is 1 - dungeon, (i.e. DP is reduce since we are getting a power up, however we must
        #ensure that DP is always >= 1, hence max(1, 1-dungeon)
        #combining both cases, the base case is max(1, 1-dungeon)
        #next thing is we will need to move from bottom right to top left until DP[0][0]
        #also when it is to decide RIGHT or DOWN, we choose the min(DP[i+1][j], DP[i][j+1])
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        #starting point at m-1, n-1
        dp[m-1][n-1] = max(1, 1-dungeon[m-1][n-1])

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                #Notice that for m-1, n-1, right and down are both None
                #hence we have to set a starting point
                right = None
                if i+1 < m:
                    right = max(1, dp[i+1][j]-dungeon[i][j])
                down = None
                if j+1 < n:
                    down = max(1, dp[i][j+1]-dungeon[i][j])

                if right and down:
                    dp[i][j] = min(right,down) #choose minimum
                elif right:
                    dp[i][j] = right
                elif down:
                    dp[i][j] = down

        return dp[0][0]