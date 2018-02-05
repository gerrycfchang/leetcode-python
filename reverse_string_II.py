"""
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result, prefix, postfix = '', '', ''

        for i in range(0, len(s), 2*k):
            if i <= len(s):
                if len(s) - i < k:
                    prefix = s[i:len(s)]
                    revStr = prefix[::-1]
                    postfix = ''
                else:
                    prefix = s[i:i + k]
                    postfix = s[i + k:i + 2 * k]
                    revStr = prefix[::-1]

                blockString = revStr + postfix
            else:
                break

            result = result + blockString
        return result


