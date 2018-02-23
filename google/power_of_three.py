"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
### log3n = log10n / log103

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        while n != 1 and n !=0 :
            if n % 3 == 0:
                n = n/3
            else:
                return False
        
        if n == 1:
            return True
    
    def isPowerOfThreeSol(self, n):
        if n <= 0: return False
        import math
        a = math.log10(n)/math.log10(3)
        return int(a) - a == 0

if __name__ == '__main__':
    sol = Solution()
    assert sol.isPowerOfThree(0) == False
    assert sol.isPowerOfThree(3) == True
    assert sol.isPowerOfThreeSol(3) == True
    assert sol.isPowerOfThreeSol(5) == False
    assert sol.isPowerOfThreeSol(-5) == False
    assert sol.isPowerOfThreeSol(81) == True