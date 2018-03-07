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
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, pstlist = [0], []
        for i in range(len(s)):            
            self.helper(s, i, i+1, res, pstlist)
            self.helper(s, i, i, res, pstlist)
        return res[0]
        
    def helper(self, s, start, end, res, pstlist):
        pstr = ''
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if start == end:
                pstr += s[start]
            else:
                pstr = s[start] + pstr + s[end]

            start -= 1
            end += 1
            res[0] += 1
            pstlist.append(pstr)


    def countSubstringsDP(self, s):
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        p  = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n): 
            dp[i][i] = 1
            p[i][i] = True

        for i in range(1,n):
            for j in range(i):
                p[i][j] = True

        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1     
                # if current string is palindrome
                if s[i] == s[j] and p[i+1][j-1]:
                    p[i][j] = True     
                #if s[i] == s[j] and s[i+1] == s[j-1]:
                if p[i][j]:
                    # Add current palindrome substring ( + 1)
                    # and rest palinrome substring (dp[i][j-1] + dp[i+1][j])
                    # remove common palinrome substrings (- dp[i+1][j-1])
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1 - dp[i+1][j-1]        
                else:
                    # Remove the duplicate part only(- dp[i+1][j-1])
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]             
        return dp[0][n - 1]
        
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.countSubstrings('abc') == 3
    assert sol.countSubstrings('aaa') == 6
    assert sol.countSubstringsDP('abc') == 3
    assert sol.countSubstringsDP('aaa') == 6
    assert sol.countSubstringsDP('fdsklf') == 6
    assert sol.countSubstringsDP("longtimenosee") == 14
    