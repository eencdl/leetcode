__author__ = 'don'
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:
    stk = []
    # @param x, an integer
    # @return an integer
    # use tuple (actual, min)
    def push(self, x):
        if len(self.stk) == 0:
            self.stk.append((x, x))
        else:
            cmin = self.stk[-1][1]
            nmin = min(x, cmin)
            self.stk.append((x, nmin))

    # @return nothing
    def pop(self):
        if len(self.stk) > 0:
            self.stk.pop()


    # @return an integer
    def top(self):
        return self.stk[-1][0]


    # @return an integer
    def getMin(self):
        return self.stk[-1][1]


if __name__ == '__main__':
    a = MinStack()
    a.push(-1)
    print a.top()
    print a.getMin()

