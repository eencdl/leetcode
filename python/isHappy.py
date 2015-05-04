class Solution:
    #use brute force if it is not happy number
    #it will
    def isHappy(self,n):
        square = dict([(c, int(c)**2) for c in '0123456789'])
        s = set()
        #check either happy or a cycle is detected
        while n != 1 and n not in s:
            s.add(n)
            n = sum(square[x] for x in str(n))
        return n == 1