# 159. Longest Substring with At Most Two Distinct Characters
# 340. Longest Substring with At Most K Distinct Characters
# 
# Given a string, find the length of the longest substring T 
# that contains at most k distinct characters.

# For example, Given s = "eceba",
# T is "ece" which its length is 3.

import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s, k):
        begin = end = length = counter = 0
        pStillNeed = collections.Counter()
        while end < len(s):
            c = s[end]
            pStillNeed[c] += 1
            if pStillNeed[c] == 1:
                counter += 1
            end += 1
            while counter > k:
                tempc = s[begin]
                pStillNeed[tempc] -= 1
                if pStillNeed[tempc] == 0:
                    counter -= 1
                begin += 1
            length = max(length, end-begin)
        return length


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLongestSubstringTwoDistinct('eceba', 2) == 3
    assert sol.lengthOfLongestSubstringTwoDistinct('abababeababbc',2) == 6
    assert sol.lengthOfLongestSubstringTwoDistinct('bbbbb',2) == 5
    assert sol.lengthOfLongestSubstringTwoDistinct('abcccbfjgi', 3) == 6
    assert sol.lengthOfLongestSubstringTwoDistinct('abcccbfjgi', 2) == 5
    assert sol.lengthOfLongestSubstringTwoDistinct('abcdbcacdbfgabcddcb', 4) == 10