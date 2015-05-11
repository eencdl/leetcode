__author__ = 'don'
"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution:
    # @param {string} digits
    # @return {string[]}
    class Solution:
    # @param {string} digits
    # @return {string[]}
    def __init__(self):
        self.result = []

    def letterCombinations(self, digits):
        if digits == '':
            return []
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.helper(digits, '', d)
        return self.result

    def helper(self, digits, r, d):
        if digits == '':
            self.result.append(r)
            return

        for c in d.get(digits[0]):
            self.helper(digits[1:], r + c, d)



if __name__ == '__main__':
    print Solution().letterCombinations('23')
