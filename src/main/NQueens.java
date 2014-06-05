package main;

import java.util.ArrayList;
import java.util.List;

/**
 The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



 Given an integer n, return all distinct solutions to the n-queens puzzle.

 Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

 For example,
 There exist two distinct solutions to the 4-queens puzzle:

 [
 [".Q..",  // Solution 1
 "...Q",
 "Q...",
 "..Q."],

 ["..Q.",  // Solution 2
 "Q...",
 "...Q",
 ".Q.."]
 ]

 */
public class NQueens {
    List<String[]> results = new ArrayList<String []>();
    public List<String[]> solveNQueens(int n) {
        //The array A[i], i is ith row,
        //A[i] contains the column
        int[] A = new int[n];
        checkMove(A,0);
        return results;
    }

    public void checkMove(int[] A, int m) {
        //Note not A.length - 1
        //we don't really check the move
        //A.length, but just use as to capture
        //the results
        if(m == A.length) {
            String[] result = new String[A.length];
            for(int i=0; i<A.length;i++){
                StringBuilder sb = new StringBuilder();
                //Fill the string with . first
                for(int j=0; j<A.length;j++)
                    sb.append('.');

                //then set the Q
                sb.setCharAt(A[i],'Q');
                result[i] = sb.toString();
            }
            results.add(result);
        } else {
            //try all possible move,
            //if valid, try next move,
            //if not keep trying
            for(int i=0; i<A.length; i++) {
                A[m] = i;
                if(isValid(A,m))
                    checkMove(A,m+1);
            }
        }
    }

    public boolean isValid(int[] A,int m) {
        //compare m with all previous placement
        for(int i=0; i<m; i++) {
            //False when it occupies the same column for different row
            //or when the diff between the row is the same as the diff
            //between the column, i.e. diagonal to each other
            if((A[i] == A[m]) || (Math.abs(A[i]-A[m]) == m-i))
                return false;
        }
        return true;
    }
}
