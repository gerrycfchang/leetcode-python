"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):                
                ns = s[0:i] + s[i + 1:len(s)]
                if ns == ns[::-1]:
                    return True
            return False
         
        """
        isPalindrome = lambda s: s == s[::-1]
        partilStr = lambda s, x: s[0:x] + s[x+1:]
        head = 0
        tail = len(s) - 1

        while head < tail:
            if s[head] != s[tail]:
                return isPalindrome(partilStr(s, head)) or isPalindrome(partilStr(s, tail))
            head += 1
            tail -= 1
        return True
        """

if __name__ == '__main__':
    sol = Solution()

    assert (sol.validPalindrome("aba") == True)
    assert (sol.validPalindrome("abca") == True)
