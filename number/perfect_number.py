"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
"""
from math import sqrt
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = set()
        if num <=1: return False
        if num > 0: res.add(1)
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                res.add (i)
                res.add(num/i)
        return sum(res) == num

if __name__ == '__main__':
    sol = Solution()

    assert sol.checkPerfectNumber(1) == False
    assert sol.checkPerfectNumber(28) == True
    assert sol.checkPerfectNumber(-6) == False