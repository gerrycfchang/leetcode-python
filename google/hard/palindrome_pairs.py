# 336. Palindrome Pairs
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
# 
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

class Solution(object):
    def palindromePairsSol1(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    temp = words[i]+words[j]
                    if temp == temp[::-1]:
                        res.append([i,j])
        return res

    def palindromePairsSol2(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(temp):
            return temp == temp[::-1]
        dict, res = {}, []
        for i in range(len(words)):
            dict[words[i][::-1]] = i
        
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)+1):
                left  = word[:j]
                right = word[j:]
                if isPalindrome(left) and right in dict and dict[right] != i:
                    if [dict[right], i] not in res:
                        res.append([dict[right], i])
                if isPalindrome(right) and left in dict and dict[left] != i:
                    if [i, dict[left]] not in res:
                        res.append([i, dict[left]]) 
        return res
        
if __name__ == '__main__':
    sol = Solution()
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    res = sol.palindromePairsSol1(words)
    res.sort()
    assert res == [[0, 1], [1, 0], [2, 4], [3,2]]

    res = sol.palindromePairsSol2(words)
    res.sort()
    assert res == [[0, 1], [1, 0], [2, 4], [3,2]]