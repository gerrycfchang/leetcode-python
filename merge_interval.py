class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        res = []
        intervals.sort(key=self.getKey)
        for i in range(len(intervals)):
            if len(res) == 0 or res[-1].end < intervals[i].start:
                res.append(intervals[i])
            else:
                if res[-1].end < intervals[i].end:
                    res[-1].end = intervals[i].end 
        return res
    
    def getKey(self, Interval):
        return Interval.start

if __name__ == '__main__':
    sol = Solution()
    int2 = Interval(1, 3)
    int1 = Interval(2, 6)
    int3 = Interval(8, 10)
    int4 = Interval(15, 18)
    num = []
    num.append(int1)
    num.append(int2)
    num.append(int3)
    num.append(int4)
    sol.merge(num)

    #assert sol.merge(num) == [[1,6],[8,10],[15,18]]

    int1 = Interval(1, 4)
    int2 = Interval(0, 4)
    num = []
    num.append(int1)
    num.append(int2)
    sol.merge(num)

    #assert sol.merge(num) == [[0, 4]]

    int1 = Interval(1, 4)
    int2 = Interval(2, 3)
    num = []
    num.append(int1)
    num.append(int2)
    sol.merge(num)

    #assert sol.merge(num) == [[1, 4]]