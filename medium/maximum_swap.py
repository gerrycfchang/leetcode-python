# 670. Maximum Swap 
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. 
# Return the maximum valued number you could get.
# 
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.# 


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        for i in range(len(s)):
            if s[i] != max(s[i:]):
                j = s[i:].rfind(max(s[i:])) + i
                return int(s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:])
        return num
if __name__ == '__main__':
    sol = Solution()
    assert sol.maximumSwap(2736) == 7236
    assert sol.maximumSwap(7236) == 7632
    assert sol.maximumSwap(9868) == 9886
    assert sol.maximumSwap(1993) == 9913
    assert sol.maximumSwap(1) == 1