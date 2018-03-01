"""

"""

from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return -1
        table = OrderedDict()
        for c in s:
            if not (c in table):
                table[c] = 1
            else:
                table[c] += 1

        index = -1
        if len(table) == 0:
            return index
        else:
            for t in table:
                if table[t] == 1:
                    index = s.find(t)
                    break
            return index

if __name__ == "__main__":
    sol = Solution()
    assert (sol.firstUniqChar('leetcode') == 0)