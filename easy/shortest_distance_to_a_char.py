# 821. Shortest Distance to a Character
# 
# Given a string S and a character C, return an array of integers 
# representing the shortest distance from the character C in the string.
# 
# Example 1:
# 
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res, pos = [], []
        for i, c in enumerate(S):
            if c == C:
                res.append(i)
                
        for i, p in enumerate(S):
            pos.append(min([abs(t-i) for t in res]))
        return pos


if __name__ == '__main__':
    obj = Solution()
    obj.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
