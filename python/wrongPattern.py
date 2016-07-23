__author__ = 'don'
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        d2 = {}
        i = 0
        words = str.split()

        if len(words) != len(pattern):
            return False

        for ch in pattern:
            if ch in d:
                if d.get(ch) != words[i]:
                    return False
            else:
                #same word should not be assign twice
                if words[i] in d2:
                    return False
                d[ch] = words[i]
                d2[words[i]] = True

            i += 1
        return True
