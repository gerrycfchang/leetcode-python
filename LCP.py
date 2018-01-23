"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class LCPSolution:
    def longestCommonPrefix (self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or strs[0][i] != string[i]:
                    return strs[0][:i]

        return strs[0]