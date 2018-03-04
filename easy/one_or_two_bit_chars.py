"""
717. 1-bit and 2-bit Characters
We have two special characters. The first character can be represented by one bit 0. 
The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. 
Return whether the last character must be a one-bit character or not. 
The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = 0
        
        while n < len(bits):
            if n == len(bits) - 1 and bits[n] == 0:
                return True            
            if bits[n] == 1:
                n += 2
            else:
                n += 1
        return False

import time
if __name__ == '__main__':
    sol = Solution()
    bits = [1, 0, 0]    
    assert sol.isOneBitCharacter(bits) == True

    bits = [1, 1, 1, 0]
    assert sol.isOneBitCharacter(bits) == False 