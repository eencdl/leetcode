__author__ = 'don'
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
class Solution:
    # @param {integer} n
    # @return {string[]}
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        # first close then open
        self.helper(n, 0, 0, '')
        return self.result

    def helper(self, n, open, close, r):

        if close == n:
            self.result.append(r)
            return

        if open > close:
            self.helper(n, open, close+1, r + ')')

        if open < n:
            self.helper(n, open+1, close, r + '(')



if __name__ == "__main__":
    print Solution().generateParenthesis(3)