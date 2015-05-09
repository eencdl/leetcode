__author__ = 'don'
"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated.
If you still see your function signature accepts a const char * argument,
please click the reload button  to reset your code definition.
"""

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if len(str) == 0:
            return 0

        str = str.lstrip().rstrip()
        str = str.lstrip('0')

        ntive = False
        if str[0] == '-':
            ntive = True
            str = str[1::]
        elif str[0] == '+':
            str = str[1::]


        r = 0
        for i in str:
            if i.isnumeric() is False:
                break
            r *= 10
            r += ord(i) - ord('0')

        if ntive:
            r = -r
        return r





