# 395. Longest Substring with At Least K Repeating Characters
#
# Find the length of the longest substring T of a given string (consists of lowercase letters only) 
# # such that every character in T appears no less than k times.
# 
# Example 1:#
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = 0
        for numUniqueTarget in range(1, 27):
            d = max(d, self.longestSubstringWithNUniqueChars(s, k, numUniqueTarget))
        return d
        
    def longestSubstringWithNUniqueChars(self, s, k, numUniqueTarget):
        begin = end = numUnique = numNoLessThanK = d = 0
        pStillNeed = collections.Counter()
        while end < len(s):
            if pStillNeed[s[end]] == 0:
                numUnique += 1
            pStillNeed[s[end]] += 1
            if pStillNeed[s[end]] == k:
                numNoLessThanK += 1
            end += 1
            while numUnique > numUniqueTarget:
                if pStillNeed[s[begin]] == k:
                    numNoLessThanK -= 1
                pStillNeed[s[begin]] -= 1
                if pStillNeed[s[begin]] == 0:
                    numUnique -= 1
                begin += 1
            if numUnique == numUniqueTarget and numUnique == numNoLessThanK:
                d = max(end - begin, d)
        return d


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestSubstring('aaabb', 3) == 3
    assert sol.longestSubstring('ababbc', 2) == 5
    
        