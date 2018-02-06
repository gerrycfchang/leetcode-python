"""

"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        ### Solution 1:
        if n <= 0:
            return False
        while n != 1 and n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        return True


        """ Solution 2:
        if n <= 0: return False
        if bin(n).count("1") == 1:
            return True
        else:
            return False
        """
