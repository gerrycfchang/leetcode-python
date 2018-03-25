# 205. Isomorphic Strings
# 
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.find(c) for c in s] == [t.find(c) for c in t]

if __name__ == '__main__':
    sol = Solution()
    assert sol.isIsomorphic('egg', 'add') == True