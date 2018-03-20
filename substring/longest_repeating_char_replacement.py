# 424. Longest Repeating Character Replacement
# 
# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. 
# Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 104.
# 
# Example 1:
# 
# Input:
# s = "ABAB", k = 2
# 
# Output:
# 4
# 
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:
# 
# Input:
# s = "AABABBA", k = 1
# 
# Output:
# 4
# 
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        begin = end = counter = length = 0
        pStillNeed = collections.Counter()
        while end < len(s):
            c = s[end]
            pStillNeed[c] += 1
            if counter < pStillNeed[c]:
                counter = pStillNeed[c]
            end += 1
            # check how many chars to "flip" by looking at the delta between the
    		# length of the string and the highest frequency char
            # If <= k, no problem. Otherwise, move window
            while end - begin - counter > k:
                tempc = s[begin]
                pStillNeed[tempc] -= 1
                counter = max(pStillNeed.values())    
                begin += 1
            length = max(length, end-begin)
        return length


if __name__ == '__main__':
    sol = Solution()
    assert sol.characterReplacement('ABAB', 2) == 4
    assert sol.characterReplacement('AABABBA', 1) == 4
    assert sol.characterReplacement('AABABAB', 3) == 7
