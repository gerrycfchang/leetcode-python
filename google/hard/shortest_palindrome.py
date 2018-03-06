
# 214. Shortest Palindrome
# refer to 5. Longest Palindromic Substring
# refer to how many pallindromes
#
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. 
# 
# Find and return the shortest palindrome you can find by performing this transformation.
# 
# For example:
# 
# Given "aacecaaa", return "aaacecaaa".
# 
# Given "abcd", return "dcbabcd".# 

class Solution(object):
    # candidate | left | right
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            return s == s[::-1]
        if isPalindrome(s): return s
        res = s
        for i in range(len(s)):
            left  = s[:i]
            right = s[i:]
            if isPalindrome(left) and len(left) >= 0:                
                if len(right) < len(res):
                    res = right[::-1]
        return res + s

    ## around center solution
    def shortestPalindromeSol(self, s):
        if len(s) <= 1: return s
        center = (len(s) - 1) / 2
        for i in range(center, -1, -1):
            if s[i] == s[i+1]:
                res = self.helper(s, i, i + 1)
                if res: return res
            
            res = self.helper(s, i, i)
            if res: return res
        return res

    def helper(self, s, start, end):
        while start >=0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        if start >= 0: return
        return s[end:][::-1] + s
                
if __name__ == '__main__':
    sol = Solution()
    assert sol.shortestPalindromeSol('aacecaaa') == sol.shortestPalindrome('aacecaaa')
    assert sol.shortestPalindromeSol('abcd') == sol.shortestPalindrome('abcd')
    assert sol.shortestPalindromeSol('aa') == sol.shortestPalindrome('aa')
    assert sol.shortestPalindromeSol('aaaa') == sol.shortestPalindrome('aaaa')
    assert sol.shortestPalindromeSol('a') == sol.shortestPalindrome('a')    
    assert sol.shortestPalindromeSol('babbbabbaba') == sol.shortestPalindrome('babbbabbaba')
    