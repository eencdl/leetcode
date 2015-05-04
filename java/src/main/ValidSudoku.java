package main;

/**
 Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

 The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

 Note:
 A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

 */
public class ValidSudoku {
    //The idea is to check all the digit to make sure there is no conflict
    //However one important thing to not is during validation
    //MUST avoid checking == c at current i,j
    public boolean isValidSudoku(char[][] board) {
        for(int i=0;i<board[0].length;i++) {
            for(int j=0; j<board.length;j++) {
                if(board[j][i] != '.') {
                    if(isValid(board,i,j) == false)
                        return false;
                }
            }
        }
        return true;
    }

    public boolean isValid(char[][] board, int i, int j) {
        char c = board[j][i];
        //check row and column for conflict
        for(int a=0; a<9;a++) {
            //check all except when a == i, for j  or a == j for i
            if( (board[a][i] == c && (a != j)) || (board[j][a] == c && (a != i)) )
                return false;
        }

        //check block for conflict
        //the division get rid of residue and then multiply by 3
        //is equivalent to floor
        for(int a=i/3*3; a<i/3*3+3;a++) {
            for(int b=j/3*3; b<j/3*3 +3;b++) {
                //Again same here check all except when a==i and b==j
                if(board[b][a] == c && !(a == i && b == j))
                    return false;
            }
        }
        return true;
    }
}
