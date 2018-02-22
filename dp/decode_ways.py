"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s=='0': return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0], dp[1] = 1, 1
        for i in range(1, len(dp)):
            if s[i-1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            if i >1 and int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.numDecodings('') == 0
    assert sol.numDecodings('0') == 0
    assert sol.numDecodings('1') == 1
    assert sol.numDecodings('10') == 1
    assert sol.numDecodings('11') == 2
    assert sol.numDecodings('101') == 1