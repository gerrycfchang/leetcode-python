# 159 Longest Substring with At Most Two Distinct Characters
# 
# Given a string, find the length of the longest substring T 
# that contains at most 2 distinct characters.

# For example, Given s = "eceba",
# T is "ece" which its length is 3.

import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        begin = end = length = counter = 0
        pStillNeed = collections.Counter()
        while end < len(s):
            c = s[end]
            pStillNeed[c] += 1
            if pStillNeed[c] == 1:
                counter += 1
            end += 1
            while counter > 2:
                tempc = s[begin]
                pStillNeed[tempc] -= 1
                if pStillNeed[tempc] == 0:
                    counter -= 1
                begin += 1
            length = max(length, end-begin)
        return length


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLongestSubstringTwoDistinct('eceba') == 3
    assert sol.lengthOfLongestSubstringTwoDistinct('abababeababbc') == 6
    assert sol.lengthOfLongestSubstringTwoDistinct('bbbbb') == 5