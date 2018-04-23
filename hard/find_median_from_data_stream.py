# 295. Find Median from Data Stream
# 
# Median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value. 
# So the median is the mean of the two middle value.
# 
# Examples: 
# [2,3,4] , the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

from heapq import heappush, heappop, heappushpop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))
        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) * 0.5
        else:
            return float(-self.small[0])

if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2.0