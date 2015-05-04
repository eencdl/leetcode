package main;

/**
 You are given an n x n 2D matrix representing an image.

 Rotate the image by 90 degrees (clockwise).

 Follow up:
 Could you do this in-place?
 */
public class RotateImage {
    //The idea is to pick one val to tmp and 4 corners
    //To make programing easy, don't add the offset k
    //first, until you got the matrix written, then
    //add offset k
    public void rotate(int[][] matrix) {
        int b = 0;                      //bottom
        int t = matrix.length - 1;      //top
        int l = 0;                      //left
        int r = matrix[0].length - 1;   //right

        while(l < r) {
            //rotate n-1 elements
            for(int k=0; k < r-l; k++) {
                //rotate all 4 corner
                int tmp = matrix[b][l+k];
                matrix[b][l+k] = matrix[t-k][l];
                matrix[t-k][l] = matrix[t][r-k];
                matrix[t][r-k] = matrix[b+k][r];
                matrix[b+k][r] = tmp;
            }
            b++;
            t--;
            l++;
            r--;
        }

    }
}
