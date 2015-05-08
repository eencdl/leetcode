__author__ = 'don'
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.lstrip().rstrip()
        if len(s) < 1:
            return 0
        i = s[::-1].find(' ')
        if i == -1:
            #only one word
            return len(s)
        else:
            return i

