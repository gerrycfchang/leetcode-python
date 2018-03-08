
# 792. Number of Matching Subsequences
# 
# Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        num = 0
        for w in words:
            index, flag = 0, True
            for c in w:
                index = S.find(c, index)
                if index == -1:
                    flag = False
                    break
                index += 1
            if flag: num += 1
        return num

if __name__ == '__main__':
    sol = Solution()
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    assert sol.numMatchingSubseq(S, words) == 3