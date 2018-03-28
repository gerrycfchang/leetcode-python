# 492. Construct the Rectangle
# 
# For a web developer, it is very important to know how to design a web page's size. 
# So, given a specific rectangular web page's area, your job by now is to design a rectangular web page, 
# whose length L and width W satisfy the following requirements:
# 
# 1. The area of the rectangular web page you designed must equal to the given target area.
# 
# 2. The width W should not be larger than the length L, which means L >= W.
# 
# 3. The difference between length L and width W should be as small as possible.
# You need to output the length L and the width W of the web page you designed in sequence.
# Example:
# Input: 4
# Output: [2, 2]

import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        res, diff = [], float('inf')
        for i in range (1, int(math.sqrt(area)) + 1):
            if area % i == 0 and area/i >= i:
                if abs(i - area/i) < diff:
                    diff = abs(i - area/i)
                    del res[::]
                    res = [area/i, i]
        return res
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.constructRectangle(1) == [1, 1]
    assert sol.constructRectangle(2) == [2, 1]