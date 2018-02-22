"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

"""

from collections import defaultdict

class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        groups = defaultdict(list)
        result = []
        for s in strings:
            temp = self.getReduceString(s)
            groups[temp].append(s)
        for key, value in groups.iteritems():
            result.append(value)
        return result

    def getReduceString(self, s):
        rstr = 'a'
        diff = 0
        if s[0] != 'a':
            diff = ord(s[0]) - ord('a')
            for i in range(1,len(s)):
                p = ord(s[i]) - diff
                if  p >= ord('a'):
                    rstr = rstr + chr(p)
                else:
                    rstr = rstr + chr(p + 26)
        else:
            rstr = s

        return rstr

if __name__ == '__main__':
    sol = Solution()

    ## case 1
    str = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

    result = sol.groupStrings(str)
    result.sort()

    exp = [
      ["abc","bcd","xyz"],
      ["az","ba"],
      ["acef"],
      ["a","z"]
    ]
    exp.sort()
    assert result == exp

    ## case 2
    str = ["abc", "cbd", "a", "z"]

    result = sol.groupStrings(str)
    result.sort()
    exp = [
      ["abc"],
        ["cbd"],
      ["a","z"]
    ]
    exp.sort()
    assert result == exp