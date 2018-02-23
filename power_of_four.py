"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num < 0: return False
        if bin(num).count('1') == 1 and (bin(num).lstrip('0').count('0')) % 2 == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()

    assert sol.isPowerOfFour(-2147483648) == False
    assert sol.isPowerOfFour(16) == True
    assert sol.isPowerOfFour(5) == False