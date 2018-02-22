"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0,i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]

if __name__ == '__main__':
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet","code"]
    assert sol.wordBreak(s, wordDict) == True
    assert sol.wordBreak('a', ['a']) == True
    assert sol.wordBreak('a', ['c']) == False
    assert sol.wordBreak('abcde', ['cde', 'ab', 'gh']) == True
    assert sol.wordBreak('cars', ['car', 'ca', 'rs']) == True
        