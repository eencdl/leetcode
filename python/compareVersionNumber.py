__author__ = 'don'
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1a = version1.split('.')
        v2a = version2.split('.')
        l1 = len(v1a)
        l2 = len(v2a)
        ml = max(l1,l2)
        for x in range(ml):
            v1 = 0
            if x < l1:
                v1 = int(v1a[x])  #int will remove preceeding zeros

            v2 = 0
            if x < l2:
                v2 = int(v2a[x])

            if v1 > v2:
                return 1

            if v2 > v1:
                return -1

        return 0
