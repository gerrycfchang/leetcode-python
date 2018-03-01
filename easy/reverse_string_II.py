"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting 
from the start of the string. If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.

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

if __name__ == '__main__':
    sol = Solution()
    assert(sol.reverseStr('a',2) == 'a')
    assert(sol.reverseStr('abcdefg',2) == 'bacdfeg')
    assert(sol.reverseStr('abcdefg',3) == 'cbadefg')
    assert(sol.reverseStr('abcdefg',8) == 'gfedcba')

