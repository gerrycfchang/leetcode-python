"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == 0 and len(needle) > 0:
            return -1
        elif len(haystack) == 0 and len(needle) == 0:
            return 0

        for i in range(len(hstr)-len(nstr)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
