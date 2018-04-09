# 131. Palindrome Partitioning
# 
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# For example, given s = "aab",
# Return
# 
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if not s: # backtracking
            res.append(path)
        for i in range(1, len(s)+1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
                
    def isPar(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    sol = Solution()
    exp = [
        ["a","a","b"],
        ["aa","b"] 
        ]
    assert sol.partition('aab') == exp