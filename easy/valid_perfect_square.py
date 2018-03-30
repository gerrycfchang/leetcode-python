# 367. Valid Perfect Square
# 
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# Input: 16
# Returns: True

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return True if int(num**0.5) * int(num**0.5) == num else False

if __name__ == '__main__':
    sol = Solution()
    assert sol.isPerfectSquare(16) == True