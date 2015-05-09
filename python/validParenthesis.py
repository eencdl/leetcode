__author__ = 'don'
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stk = []
        d = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i == ')' or i == ']' or i=='}':
                if len(stk) == 0 or stk[-1] != i:
                    return False
                stk.pop()
            else:
                stk.append(d[i])
        if len(stk) == 0:
            return True
        else:
            return False