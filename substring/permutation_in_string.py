# 567. Permutation in String
# 
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False

import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        begin = end = 0
        pStillNeed = collections.Counter(s1)
        counter = len(pStillNeed)
        while end < len(s2):
            c = s2[end]
            if c in pStillNeed:
                pStillNeed[c] -= 1
                if pStillNeed[c] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                tempc = s2[begin]
                if tempc in pStillNeed:
                    pStillNeed[tempc] += 1
                    if pStillNeed[tempc] > 0:
                        counter += 1
                if len(s1) ==  end - begin:
                    return True
                begin += 1
        return False
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.checkInclusion('ab', 'eidbaooo') == True
    assert sol.checkInclusion('ab', 'eidboaoo') == False