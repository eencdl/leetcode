package main;

/**
 Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

 You have the following 3 operations permitted on a word:

 a) Insert a character
 b) Delete a character
 c) Replace a character

 */
public class EditDistance {
    //Using 2 dimention DP, rows represent word1, column represent word2 to solve this
    //word1[i] == word2[j] ,  dp[i][j] = dp[i][j]   , cost = 0
    //for word1[i] != word2[j], cost = 1 as follows:
    //dp[i][j] = dp[i-1][j-1] + 1 , (replace), i.e. now word1[i] == word2[j]
    //dp[i][j] = dp[i-1][j] + 1   , (remove) , i.e. word1 remove 1 char, but might not still match word2[j]
    //dp[i][j] = dp[i][j-1] + 1   , (insert),  i.e. word1 insert 1 char, will match word2[j],
    //                                          but word1 stay at i since one match and one insert cancel out
    //So the goal is to pick the minimum cost among 3 types of operations, and consider all of them
    public int minDistance(String word1, String word2) {
        int l1 = word1.length();
        int l2 = word2.length();

        //Initial condition needed
        //else the nested for loop will not work
        if(l1 == 0) return l2;
        if(l2 == 0) return l1;

        int[][] dp = new int[l1+1][l2+1];

        //initial condition
        //assuming word2 is an empty string
        for(int i=0; i<=l1; i++) {
            dp[i][0] = i;
        }

        //assuming word1 is an empty string
        for(int j=1; j<=l2; j++) {
            dp[0][j] = j;
        }

        char[] w1 = word1.toCharArray();
        char[] w2 = word2.toCharArray();

        for(int i=0; i<l1; i++) {
            for(int j=0; j<l2; j++) {
                if(w1[i] == w2[j]) {
                    dp[i+1][j+1] = dp[i][j];
                } else {
                    //The minimum of 3 methods
                    dp[i+1][j+1] = Math.min(Math.min(dp[i][j]+1, dp[i][j+1]+1),dp[i+1][j]+1);
                }
            }
        }
        return dp[l1][l2];
    }
}
