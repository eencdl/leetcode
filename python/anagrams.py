__author__ = 'don'
"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        for word in strs:
            key = ''.join(sorted(word))
            d[key] = [word] if key not in d else d[key] + [word]

        r = []
        for item in d:
            #this is important as if only 1, there is no anagram
            if len(d[item]) >= 2:
                r += d[item]
        return r

