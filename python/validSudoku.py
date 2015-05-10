__author__ = 'don'
"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.
Each row must have the numbers 1-9 occuring just once.
Each column must have the numbers 1-9 occuring just once.
Each 3x3 grid must have the numbers 1-9 occuring just once.
"""
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # create one vector for each check
        # row, column, 3x3 grid
        # the tricky about 3x3 grid use (i/3)*3 + (j/3)
        row = [[False for i in xrange(9)] for j in xrange(9)]
        col = [[False for i in xrange(9)] for j in xrange(9)]
        grid = [[False for i in xrange(9)] for j in xrange(9)]
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j]) - 1
                if row[i][num] or col[j][num] or grid[(i/3)*3 + (j/3)][num]:
                    return False
                else:
                    row[i][num], col[j][num], grid[(i/3)*3 + (j/3)][num] = True, True, True

        return True
