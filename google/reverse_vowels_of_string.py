"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import OrderedDict
        vdict = OrderedDict()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vlist, vkeys, vvalue = [], [], []
        for i in range(len(s)):
            if s[i] in vowels:
                vdict[i] = s[i]
            vlist.append(s[i])
        for key, value in vdict.iteritems():
            vkeys.append(key)
            vvalue.append(value)
        vvalue = vvalue[::-1]
        for i in vkeys:
            vlist[i] = vvalue.pop(0)

        return "".join(vlist)


