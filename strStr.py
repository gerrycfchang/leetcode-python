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

        hstr = list(haystack)
        nstr = list(needle)

        if len(hstr) < len(nstr):
            return -1
        elif len(haystack) == 0 and len(needle) > 0:
            return -1
        elif len(haystack) == 0 and len(needle) == 0:
            return 0

        for i in range(len(hstr)-len(nstr)+1):
            if hstr[i:i+len(nstr)] == nstr:
                return i

        return -1
