# 242. Valid Anagram
# 
# Given two strings s and t, write a function to determine if t is an anagram of s.
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)

if __name__ == '__main__':
    sol = Solution()
    assert sol.isAnagram('anagram','nagaram') == True
        