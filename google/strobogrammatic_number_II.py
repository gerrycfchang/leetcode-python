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

if __name__ == '__main__':
    sol = Solution()
    exp = ["11","69","88","96"]
    assert (sol.findStrobogrammatic(2) == exp)

    exp = ["101", "609", "808", "906", "111", "619", "818", "916", "181", "689", "888", "986"]
    assert ((sol.findStrobogrammatic(3) == exp))

    exp = ["1001", "6009", "8008", "9006", "1111", "6119", "8118", "9116", "1691", "6699",
            "8698", "9696", "1881", "6889", "8888", "9886", "1961", "6969", "8968", "9966"]
    assert ((sol.findStrobogrammatic(4) == exp))