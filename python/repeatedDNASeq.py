__author__ = 'don'
"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
class Solution:
    #just use hashtable
    def findRepeatedDnaSequences(self, s):
        d = {}
        r = []
        l = len(s)
        for i in range(l-9):
            w = s[i:i+10]
            d[w] = d.get(w, 0) + 1
        for k, v in d.items():
            if v > 1:
                r.append(k)
        return r