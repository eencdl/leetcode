__author__ = 'don'
"""
Given a string, determine if a permutation of the string could form a palindrome.
For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
class Solution(object):
    def palindromePermutation(self, s):
        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        odd = 0
        for k, v in d.iteritems():
            if v % 2 == 1:
                odd += 1
        return odd <= 1

if __name__ == '__main__':
    print Solution().palindromePermutation('aab')
    print Solution().palindromePermutation('carerac')
    print Solution().palindromePermutation('abba')
    print Solution().palindromePermutation('aabdaq')