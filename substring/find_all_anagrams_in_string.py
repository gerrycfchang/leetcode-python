# 438. Find All Anagrams in a String
# 
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pStillNeed = collections.Counter(p)
        counter = len(pStillNeed)
        begin = end = 0

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
                if end-begin == len(p):
                    res.append(begin)
                begin += 1
        return res

    def findAnagramsSlidingWindow(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, res = len(p), []
        pCounter, sCounter = collections.Counter(p), collections.Counter(s[:n-1])
        for i in range(n-1, len(s)):
            sCounter[s[i]] += 1
            if pCounter == sCounter:
                res.append(i-n+1)
            sCounter[s[i-n+1]] -= 1
            if sCounter[s[i-n+1]] == 0:
                del sCounter[s[i-n+1]]
        return res
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.findAnagrams('cbaebabacd', 'abc') == [0, 6]
    assert sol.findAnagrams('abab', 'ab') == [0, 1, 2]
    assert sol.findAnagramsSlidingWindow('cbaebabacd', 'abc') == [0, 6]
    assert sol.findAnagramsSlidingWindow('abab', 'ab') == [0, 1, 2]