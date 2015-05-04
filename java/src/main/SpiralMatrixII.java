package main;

/**
 Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

 For example,
 Given n = 3,

 You should return the following matrix:
 [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
 ]
 */
public class SpiralMatrixII {
    //The idea is if we have not get to n2
    //we had not finish the spiral
    public int[][] generateMatrix(int n) {
        int i = 1;
        int lastnum = n*n;
        int b = 0;      //bottom
        int t = n-1;    //top
        int l = 0;      //left
        int r = n-1;    //right
        int[][] m = new int[n][n];

        while(i <= lastnum) {
            //left to right
            for(int j=l;j<=r;j++) {
                m[b][j] = i++;
            }
            b++;

            //bottom to top
            for(int j=b;j<=t;j++) {
                m[j][r] = i++;
            }
            r--;

            //right to left
            for(int j=r;j>=l;j--){
                m[t][j] = i++;
            }
            t--;

            //top to bottom
            for(int j=t;j>=b;j--){
                m[j][l] = i++;
            }
            l++;
        }
        return m;
    }
}
