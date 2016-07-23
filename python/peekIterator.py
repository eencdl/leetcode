__author__ = 'don'
"""
"""
# Below is the interface for Iterator, which is already defined for you.
#


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.index = 0
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.index += 1
        return self.nums[self.index-1]


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        if iterator.hasNext():
            self.nv = iterator.next()
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nv

    def next(self):
        """
        :rtype: int
        """
        t = self.nv
        if self.iterator.hasNext():
            self.nv = self.iterator.next()
        else:
            self.nv = None
        return t

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nv is not None


i = [1, 2, 3, 4]
cmds = [0, 1, 1, 2, 2, 1, 1, 2, 0, 1, 0, 2, 0]
pio = PeekingIterator(Iterator(i))
r = []
for cmd in cmds:

    if cmd == 0:
        r.append(pio.hasNext())
    elif cmd == 1:
        r.append(pio.peek())
    elif cmd == 2:
        r.append(pio.next())

print r