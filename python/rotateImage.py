__author__ = 'don'
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        tp, bt, lf, rg, w = 0, n - 1, 0, n - 1, n-1
        while bt-tp >= 1:
            for i in range(w):
                tmp = matrix[tp][lf + i]
                matrix[tp][lf + i] = matrix[bt - i][lf]
                matrix[bt - i][lf] = matrix[bt][rg - i]
                matrix[bt][rg - i] = matrix[tp + i][rg]
                matrix[tp + i][rg] = tmp
            tp += 1
            bt -= 1
            lf += 1
            rg -= 1
            w -= 2

if __name__ == '__main__':
    print Solution().rotate([[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]])







