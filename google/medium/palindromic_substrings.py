# 647. Palindromic Substrings
#
# Given a string, your task is to count how many palindromic substrings in this string.
# 
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
# 
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".# 


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [0]
        for i in range(len(s)):            
            self.helper(s, i, i+1, res)
            self.helper(s, i, i, res)
        return res[0]
        
    def helper(self, s, start, end, res):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            res[0] += 1
        
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.countSubstrings('abc') == 3
    assert sol.countSubstrings('aaa') == 6