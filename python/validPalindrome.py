__author__ = 'don'
"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = s.lower()
        newS = []
        for i in s:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                newS.append(i)
        return newS == newS[::-1]