__author__ = 'don'
"""
write code to interpret statements
(add 1 2)
(add (mult 2 3) (mult 2 2))
(add 3 (mult 2 3))

Extension
(let x 5 (add x 3))
(let x 5 (add x (let x 6 (mult 2 x))))
"""

class Solution:

    def math(self, stmt):
        stk, d, vstk = [], {}, []
        stmt = stmt.replace('(', '')
        stmt = stmt.replace(')', '')
        items = stmt.split()
        p1, fr, var = None, False, None
        for i in items:
            #this part extract from 'let'
            if len(stk) > 0 and fr:
                if i.isdigit():
                    d.get(var).append(int(i))
                    fr = False
                else:
                    var = i
                    if var not in d:
                        d[var] = []
                    vstk.append(var)
            elif i.isdigit() or i in d:
                #found the operand
                v = int(i) if i not in d else d.get(i)[-1]

                if p1 is None:
                    p1 = v
                else:
                    ops = stk.pop()
                    while ops == 'let':
                        v2 = vstk.pop()
                        d.get(v2).pop()
                        ops = stk.pop()

                    if ops == 'add':
                        p1 += v
                    elif ops == 'mult':
                        p1 *= v

                    while len(stk) > 0 and type(stk[-1]) is int:
                        v = stk.pop()
                        ops = stk.pop()
                        while ops == 'let':
                            v2 = vstk.pop()
                            d.get(v2).pop()
                            ops = stk.pop()
                        if ops == 'add':
                            p1 += v
                        elif ops == 'mult':
                            p1 *= v
                    while len(stk) > 0 and stk[-1] == 'let':
                        v2 = vstk.pop()
                        d.get(v2).pop()
                        stk.pop()
            else:
                if i == 'let':
                    fr = True
                else:
                    if p1 is not None:
                        stk.append(p1)
                        p1 = None
                stk.append(i)
        return p1

if __name__ == '__main__':
    print Solution().math('(let x 5 (add (let x 6 (mult 2 x)) x))')
    #print Solution().math('(add (mult 2 3) (mult 2 (mult 4 5)))')

