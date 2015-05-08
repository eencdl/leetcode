__author__ = 'don'
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same character
but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        #Need 2 dic to crossmap
        st, ts = dict(), dict()
        for i in range(len(t)):
            t1, s1 = st.get(s[i]), ts.get(t[i])
            if s1 is None and t1 is None:
                st[s[i]], ts[t[i]] = t[i], s[i]
            elif s1 != s[i] or t1 != t[i]:
                return False
        return True


if __name__ == '__main__':
    print Solution().isIsomorphic('ab', 'aa')
