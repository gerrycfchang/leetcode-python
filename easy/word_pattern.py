# 290. Word Pattern
# 
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# 
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        slist = str.split()
        return map(pattern.find, pattern) == map(slist.index, slist)
        

if __name__ == '__main__':
    sol = Solution()
    pattern = "abba"
    string = "dog cat cat dog"
    assert sol.wordPattern(pattern, string) == True