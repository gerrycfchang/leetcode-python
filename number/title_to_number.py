"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        for i in range(len(s)):
            result = result + (ord(s[i]) - 64) * (26 ** (len(s) - i - 1))

        return result