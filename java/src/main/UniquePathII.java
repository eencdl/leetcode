package main;

/**
 Follow up for "Unique Paths":

 Now consider if some obstacles are added to the grids. How many unique paths would there be?

 An obstacle and empty space is marked as 1 and 0 respectively in the grid.

 For example,
 There is one obstacle in the middle of a 3x3 grid as illustrated below.

 [
 [0,0,0],
 [0,1,0],
 [0,0,0]
 ]
 The total number of unique paths is 2.

 Note: m and n will be at most 100.
 */
public class UniquePathII {
    //You can use DP approach here to minimize stack burden
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int r = obstacleGrid.length;
        int c = obstacleGrid[0].length;
        int[][] dp = new int[r][c];

        if(obstacleGrid[0][0] == 1) return 0; //starting point is an obstacle
        dp[0][0] = 1;

        //Initialization, moving from
        //left to right
        for(int i=1;i<c;i++){
            if(obstacleGrid[0][i] != 1)
                dp[0][i] = dp[0][i-1];
        }

        //Initialization, moving from
        //up to down
        for(int j=1;j<r;j++) {
            if(obstacleGrid[j][0] != 1)
                dp[j][0] = dp[j-1][0];
        }

        //Now as we move, there might be 2 path for
        //each corresponding point, hence
        for(int j=1;j<r;j++) {
            for(int i=1;i<c;i++){
                if(obstacleGrid[j][i] != 1)
                    dp[j][i] = dp[j-1][i] + dp[j][i-1];
            }
        }
        return dp[r-1][c-1];
    }
}
