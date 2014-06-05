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
    ArrayList<String> results = new ArrayList<String>();
    public List<String[]> solveNQueens(int n) {



    }

    public void checkMove(int[] A, int m) {
        if(m == A.length-1) {
            String[] result = new String[A.length];
            for(int i=0; i<A.length;i++){
                StringBuilder sb = new StringBuilder("........");
                sb.setCharAt(A[i],'Q');
                result[i] = sb.toString();
            }
            results.add(result);
        } else {
            //try all possible move
            for(int i=0; i<A.length; i++) {
                A[m] = i;
                if(isValid(A,m))
                    checkMove(A,m+1);
            }
        }
     }

    public boolean isValid(int[] A,int m) {
        for(int i=0; i<m; i++) {
            if(A[i] == A[m] || (Math.abs(A[i]-A[m])) == m-i))
                return false;
        }
        return true;
    }
}
