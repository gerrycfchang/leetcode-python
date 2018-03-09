# 281. Zigzag Iterator
# 
# Given two 1d vectors, implement an iterator to return their elements alternately.
# 
# For example, given two 1d vectors:
# 
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, 
# 
# the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].


class ZigzagIterator(object):
    def __init__(self, l1, l2):
        n1, n2 = len(l1), len(l2)
        self.res = []
        for i in range(n1+n2):
            if i<n1: self.res.append(l1[i])
            if i<n2: self.res.append(l2[i])

    def next(self):
        """
        :rtype: int
        """
        return self.res.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.res) != 0

if __name__ == '__main__':
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    zig = ZigzagIterator(v1, v2)
    res = []
    while zig.hasNext():
        res.append(zig.next())
    assert res == [1, 3, 2, 4, 5, 6]
