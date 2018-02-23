"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if bin(n).count('1') == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    assert sol.isPowerOfTwo(2) == True
    assert sol.isPowerOfTwo(3) == False
    assert sol.isPowerOfTwo(1024) == True