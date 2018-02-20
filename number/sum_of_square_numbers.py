"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0: return True
        
        import math
        a = 1
        while a*a < c+1:
            b = int(math.sqrt(c - a**2))
            if b**2 + a**2 == c:
                return True
            a += 1
        return False

if __name__ == '__main__':
    sol = Solution()
    assert sol.judgeSquareSum(0) == True
    assert sol.judgeSquareSum(3) == False
    assert sol.judgeSquareSum(5) == True