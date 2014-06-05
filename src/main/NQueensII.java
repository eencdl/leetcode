package main;

/**
 Follow up for N-Queens problem.

 Now, instead outputting board configurations, return the total number of distinct solutions.
 */
public class NQueensII {
    //This is easy, please refer to NQueens
    //to see how we achieve this
    //basically just increment counter
    //when we reach a solution
    int cnt = 0;
    public int totalNQueens(int n) {
        int[] A = new int[n];
        checkMove(A,0);
        return cnt;
    }

    public void checkMove(int[] A, int m) {
        if(m == A.length) {
            cnt++;
        } else {
            for(int i=0; i<A.length;i++){
                A[m] = i;
                if(isValid(A,m))
                    checkMove(A,m+1);
            }
        }
    }


    public boolean isValid(int[] A, int m) {
        for(int i=0; i<m; i++) {
            if((A[i] == A[m]) || (Math.abs(A[i] - A[m]) == m-i))
                return false;
        }
        return true;
    }
}
