# 76. Minimum Window Substring
# 
# Given a string S and a string T, find the minimum window in S 
# which will contain all the characters in T in complexity O(n).
# 
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC"


import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        pStillNeed = collections.Counter(t)
        head = begin = end = 0
        counter, maxLen = len(pStillNeed), float('inf')
        while end < len(s):
            c = s[end]
            if c in pStillNeed:
                pStillNeed[c] -= 1
                if pStillNeed[c] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                tempc = s[begin]
                if tempc in pStillNeed:
                    pStillNeed[tempc] += 1
                    if pStillNeed[tempc] > 0:
                        counter += 1
                if end - begin< maxLen:
                    maxLen = end - begin
                    head = begin
                begin += 1
        return s[head:head+maxLen] if maxLen != float('inf') else ''                   
        
        

if __name__ == '__main__':
    sol = Solution()
    sol.minWindow("ADOBECODEBANC", 'ABC') == 'BANC'
    sol.minWindow("ab", 'a') == 'a'