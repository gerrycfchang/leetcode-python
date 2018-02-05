"""
Description:

Count the number of prime numbers less than a non-negative number, n.

"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 0
        
        digits = [1]*n
        digits[0] = digits[1] = 0

        for i in range(2, int(n ** 0.5)+1):
            if digits[i] == 1:
                for j in range(i * 2,n,i):
                    digits[j] = 0

        return sum(digits)
