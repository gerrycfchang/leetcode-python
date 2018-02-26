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

    def reverseWordsSol(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s.strip(' ')) == 0: return ''
        slist = s.split()
        slist = slist[::-1]
        return ' '.join(slist)

if __name__ == '__main__':
    sol = Solution()

    inp = "the sky is blue"
    exp = 'blue is sky the'
    assert (sol.reverseWordsSol(inp) == exp)

    inp = " a"
    exp = 'a'
    assert (sol.reverseWordsSol(inp) == exp)

    inp = " "
    exp = ''
    assert (sol.reverseWordsSol(inp) == exp)

