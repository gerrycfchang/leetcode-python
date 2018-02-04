"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        s = s.lower()
        import re
        s = re.sub(r'[?|$|.|!]', r'', s)
        s = re.sub(r'^A-Za-z0-9+', '', s)
        rstr = s[::-1]

        return s == rstr
