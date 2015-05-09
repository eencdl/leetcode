__author__ = 'don'
"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        y = len(strs[0])
        print strs[1][1]
        for i in range(1, len(strs)):
            y = min(y, len(strs[i]))
            for j in range(0, y, 1):
                if strs[0][j] != strs[i][j]:
                    y = j
                    break
        return strs[0][0:y]


if __name__ == "__main__":
    print Solution().longestCommonPrefix(["aa", "ab"])