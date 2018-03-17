# 657. Judge Route Circle
# 
# Initially, there is a Robot at position (0, 0). 
# Given a sequence of its moves, judge if this robot makes a circle, 
# which means it moves back to the original place.
# 
# The move sequence is represented by a string. And each move is represent by a character. 
# The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
# The output should be true or false representing whether the robot makes a circle.
# 
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false
import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lrqueue, udqueue = [], []
        for c in moves:
            if c == 'U':
                udqueue.append(1)
            elif c == 'D':
                udqueue.append(-1)
            elif c == 'R':
                lrqueue.append(1)
            else:
                lrqueue.append(-1)
        return True if sum(lrqueue) + sum(udqueue) == 0 else False

    def judgeCircleSol(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = collections.Counter(moves)
        return True if c['U'] == c['D'] and c['L'] == c['R'] else False
    
                
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.judgeCircle('UD') == True
    assert sol.judgeCircle('LL') == False

    assert sol.judgeCircleSol('UD') == True
    assert sol.judgeCircleSol('LL') == False