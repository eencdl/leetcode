__author__ = 'don'
"""
Given a string s and a dictionary of words dict,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        # segment cut before first char and after last char
        # assumption is that the dict doesn't have the entire word leetcode
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            for k in range(i):
                # previous segment is true and the char from k to i is in dict
                if dp[k] and s[k:i] in wordDict:
                    dp[i] =True
        return dp[len(s)]



