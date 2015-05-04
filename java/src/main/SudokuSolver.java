package main;

/**
 Write a program to solve a Sudoku puzzle by filling the empty cells.

 Empty cells are indicated by the character '.'.

 You may assume that there will be only one unique solution.

 all columns, rows and block should not conflict

 9 queens problem
 */
public class SudokuSolver {
    public void solveSudoku(char[][] board) {
        if(board == null || board.length == 0)
            return;

        solved(board);
    }
    public boolean solved(char[][] board) {
        for(int i=0;i<board[0].length;i++) {
            for(int j=0; j<board.length;j++) {
                if(board[j][i] == '.') {
                    for(char k='1'; k<='9'; k++) {
                        //check for conflict, before assigning
                        //the trial value
                        //very important !!
                        if(isValid(board,i,j,k)) {
                            board[j][i] = k;
                            //Do it recursively, after assigning
                            //trial value
                            if(solved(board)) {
                                return true; //at this point it returns
                            } else {
                                //Putting back all the trial
                                //value that fail
                                board[j][i] = '.';
                            }
                        }
                    }
                    return false; //no solution after trying all possible k
                }
            }
        }
        return true; //finish all the last return
   }

    public boolean isValid(char[][] board, int i, int j,char c) {
        //check row and column for conflict
        for(int a=0; a<9;a++) {
            if(board[a][i] == c || board[j][a] == c)
                return false;
        }

        //check block for conflict
        //the division get rid of residue and then multiply by 3
        //is equivalent to floor
        for(int a=i/3*3; a<i/3*3+3;a++) {
            for(int b=j/3*3; b<j/3*3 +3;b++) {
                if(board[b][a] == c)
                    return false;
            }
        }
        return true;
    }
}
