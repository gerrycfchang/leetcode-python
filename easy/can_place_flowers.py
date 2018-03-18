# 605. Can Place Flowers
# 
# Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
# However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, 
# where 0 means empty and 1 means not empty), and a number n, 
# return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
            
        return True if count >= n else False
            
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.canPlaceFlowers([1,0,0,0,1], 1) == True
    assert sol.canPlaceFlowers([1,0,0,0,1], 2) == False
    assert sol.canPlaceFlowers([0,0,1,0,1], 1) == True