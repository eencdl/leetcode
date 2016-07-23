__author__ = 'don'
"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
"""
import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.maxheap) == 0:
            self.maxheap = [-num]
        else:
            if len(self.maxheap) >= len(self.minheap):
                if num >= -self.maxheap[0]:
                    heapq.heappush(self.minheap, num)
                else:
                    heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                    heapq.heappush(self.maxheap, -num)
            else:
                if num <= self.minheap[0]:
                    heapq.heappush(self.maxheap, -num)
                else:
                    heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                    heapq.heappush(self.minheap, num)


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxheap) == 0:
            return 0
        elif len(self.minheap) == 0:
            return -self.maxheap[0]
        elif len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0])/2.0
        else:
            return self.minheap[0] if len(self.minheap) > len(self.maxheap) else -self.maxheap[0]
            

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(-1)
mf.addNum(-2)
mf.addNum(3)
mf.addNum(4)

print mf.findMedian()