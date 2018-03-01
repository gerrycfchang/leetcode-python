"""
Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
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

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    hstr = 'hello'
    str = 'll'
    assert(sol.strStr(hstr,str) == 2)

    hstr = 'aaaaa'
    str = 'bba'
    assert(sol.strStr(hstr,str) == -1)

    hstr = ''
    str = 'bba'
    assert(sol.strStr(hstr,str) == -1)

    hstr = ''
    str = ''
    assert(sol.strStr(hstr,str) == 0)

    hstr = 'a'
    str = 'a'
    assert(sol.strStr(hstr,str) == 0)
