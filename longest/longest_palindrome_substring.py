# 5. Longest Palindromic Substring
# refer to 214. Shortest Palindrome
# refer to howmanyPalindrome
# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.
# 
# Example:
# 
# Input: "babad"
# 
# Output: "bab"
# 
# Note: "aba" is also a valid answer.
#  
# 
# Example:
# 
# Input: "cbbd"
# 
# Output: "bb"# 

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=1: return s
        dp = [[False for _ in range (len(s))] for _ in range(len(s))]
        start, maxlen = -1, 0
        for j in range(len(s)):
            for i in range(0,j+1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i]==s[j]
                elif j - i > 1:
                    if dp[i+1][j-1] and s[i]==s[j]:
                        dp[i][j] = True
                if dp[i][j]:
                    if j - i + 1 > maxlen:
                        start = i
                        maxlen = j-i+1
        return s[start:start+maxlen]
    
    def arroundCenterLongestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestStr = ''
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(longestStr):
                longestStr = temp
            
            temp = self.helper(s, i, i+1)
            if len(temp) > len(longestStr):
                longestStr = temp
        return longestStr

    def helper(self, s, start, end):
        while start >=0 and end < len(s) and s[start]==s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
                    

if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindrome('') == ''
    assert sol.longestPalindrome('a') == 'a'
    assert sol.longestPalindrome('babad') == 'bab'
    assert sol.longestPalindrome('abadcaacbddd') == 'caac'
    longestStr = ("abababababababababababababababababababababab" 
    "ababababababababababababababababababababababababababababab"  
    "ababababababababababababababababababababababababababababab" 
    "ababababababababababababababababababababababababababababab" 
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "ababababababababababababababababababababababababababababab"
    "abababababababababababababa")
    #reStr = sol.longestPalindrome(longestStr)
    #assert  reStr == longestStr

    assert sol.arroundCenterLongestPalindrome('abadcaacbddd') == 'caac'
    assert sol.arroundCenterLongestPalindrome(longestStr) == longestStr