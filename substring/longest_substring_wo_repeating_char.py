# 3. Longest Substring Without Repeating Characters
# 
# Given a string, find the length of the longest substring without repeating characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        start, dup , dp = 0, {}, [0] * len(s)
        dp[0] = 1
        dup[s[0]] = 0
        for i in range (1, len(s)):
            if s[i] in dup and start <= dup[s[i]]:
                start = dup[s[i]] + 1
                dp[i] = dp[i-1]
            else:                    
                dp[i] = max(dp[i-1], i-start+1)
            dup[s[i]] = i    
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring('abcabcbb') == 3
    assert sol.lengthOfLongestSubstring('bbbbb') == 1
    assert sol.lengthOfLongestSubstring('dvdf') == 3
    assert sol.lengthOfLongestSubstring('pwwkew') == 3
    assert sol.lengthOfLongestSubstring('tmmzuxt') == 5