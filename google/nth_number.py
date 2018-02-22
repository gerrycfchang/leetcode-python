"""

"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digitType = 1
        digitNum= 9
        while n > digitType * digitNum:
            n = n - digitType * digitNum
            digitType += 1
            digitNum *= 10
        n -= 1
        realNum = (n/digitType) + 10 ** (digitType - 1)
        return int(str(realNum)[n % digitType])

if __name__ == '__main__':
    sol = Solution()
    assert sol.findNthDigit(13) == 1
    assert sol.findNthDigit(3) == 3