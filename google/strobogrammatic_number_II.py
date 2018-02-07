"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

"""

class Solution(object):
    def findStrobogrammatic(self, n):
        return self.helper(n, n)

    def helper(self, m, n):
        result = []
        if m == 0: return ['']
        if m == 1: return ['0', '1', '8']
        if m > 1: temp = self.helper(m - 2, n)
        for i in temp:
            if m != n: result.append('0' + i + '0')
            result.append('1' + i + '1')
            result.append('6' + i + '9')
            result.append('8' + i + '8')
            result.append('9' + i + '6')

        return result