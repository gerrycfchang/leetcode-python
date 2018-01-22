"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        if x >= 0:
            rstring = string[::-1]
        else:
            rstring = '-' + string[:0:-1]

        finalnum = int(rstring)
        if finalnum > 2 ** 31 - 1:
            finalnum = 0
        elif finalnum < -1 * 2 ** 31:
            finalnum = 0
        return finalnum

if __name__ == '__main__':
    sol = Solution()
    result = sol.reverse(120)
    print result
    result = sol.reverse(-120)
    print result
    result = sol.reverse(0)
    print result
    result = sol.reverse(-123)
    print result
    result = sol.reverse(1534236469)
    print result
    result = sol.reverse(900000)
    print result
    result = sol.reverse(1563847412)
    print result
    result = sol.reverse(-1563847412)
    print result
