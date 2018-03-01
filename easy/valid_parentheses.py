"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isValid = False
        array = []
        if s == '':
            return False

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                array.append(s[i])
            else:
                if len(array) == 0:
                    symbol = ''
                else:
                    symbol = array.pop()

                if s[i] == ')' and symbol == '(':
                    isValid = True
                elif s[i] == ']' and symbol == '[':
                    isValid = True
                elif s[i] == '}' and symbol == '{':
                    isValid = True
                else:
                    return False

        if len(array) == 0:
            isValid = True
        else:
            isValid = False

        return isValid

if __name__ == '__main__':
    sol = Solution()
    assert(sol.isValid('()(())') == True)
    assert(sol.isValid('(){}[]') == True)
    assert(sol.isValid('(]') == False)
    assert(sol.isValid('') == False)
    assert(sol.isValid('((({})[]){})') == True)
    assert(sol.isValid(']') == False)