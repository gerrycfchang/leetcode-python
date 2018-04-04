# 441. Arranging Coins
# 
# You have a total of n coins that you want to form in a staircase shape, 
# 
# where every k-th row must have exactly k coins.
# 
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n <= 1: return n
        k = 1
        while ((1+k) * k) / 2 <= n:
            k += 1
        return k - 1


if __name__ == '__main__':
    sol = Solution()
    assert sol.arrangeCoins(5) == 2
        