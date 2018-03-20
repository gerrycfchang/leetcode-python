# 409. Longest Palindrome
# 
# Given a string which consists of lowercase or uppercase letters, 
# 
# find the length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# Example:
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter, c = collections.Counter(s), 0
        for value in counter.values():
            if value % 2 == 1:
                c += 1
        return len(s) - c + 1 if c else len(s)
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindrome('abccccdd') == 7
    assert sol.longestPalindrome('ccc') == 3
    assert sol.longestPalindrome('bb') == 2