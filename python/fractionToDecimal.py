__author__ = 'don'
"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""


class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        #find out if negative
        isNegative = False
        if numerator*denominator < 0:
            isNegative = True

        numerator = abs(numerator)
        denominator = abs(denominator)

        nlist = [] #numlist keep track of integer
        d = {} #keep track of cycles
        pos = 0
        loopStr = None
        while True:
            nlist.append(str(numerator/denominator)) #only get the integral part
            r = numerator % denominator #calculate remainder
            pos += 1 #current position in the division

            #completely dividable
            if r == 0:
                break

            #new numerator
            numerator = r * 10

            #check for looping
            loc = d.get(numerator)
            if loc:
                #cycle detected
                loopStr = "".join(nlist[loc:pos])
                break

            d[numerator] = pos

        ans = nlist[0] #integral part
        #decimal needed
        if len(nlist) > 1:
            ans += '.'

        if loopStr:
            #concatenate non-loop integer + (looping integers)
            ans += "".join(nlist[1:len(nlist) - len(loopStr)]) + "(" + loopStr + ")"
        else:
            #no loop straight forward
            ans += "".join(nlist[1:])

        if isNegative:
            ans = "-" + ans

        return ans