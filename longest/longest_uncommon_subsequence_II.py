# 522. Longest Uncommon Subsequence II
# 
# Given a list of strings, you need to find the longest uncommon subsequence among them. 
# 
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings 
# 
# and this subsequence should not be any subsequence of the other strings.
# 
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. 
# 
# Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
# 
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. 
# 
# If the longest uncommon subsequence doesn't exist, return -1.
# 
# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def issubsequence(s1, s2):
            i = 0
            for c in s2:
                if i < len(s1) and s1[i] == c:
                    i += 1
            return len(s1) == i
        strs.sort(key=len, reverse=True)
        for i in range(len(strs)):
            for j in range(len(strs)):
                if issubsequence(strs[i], strs[j]) and j != i: break
                elif j == len(strs) - 1:
                    return len(strs[i])
        return -1

if __name__ == '__main__':
    sol = Solution()
    strs = ['aba','cdc','eae']
    assert sol.findLUSlength(strs) == 3