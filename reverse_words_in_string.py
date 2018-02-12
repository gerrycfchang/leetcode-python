"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s.strip(' ')) == 0: return ""
        res = s.split(' ')
        str = ''
        for i in range(len(res) - 1, -1, -1):
            str = str.strip(' ') + " " + res[i]

        return str.strip(' ')

