# 318. Maximum Product of Word Lengths
# 
# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
# where the two words do not share common letters. 
# 
# You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
# 
# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
# 
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
# 
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.

#  Logic
#  The soultion is calcuated by doing a product of the length of
#  each string to every other string. Anyhow the constraint given is
#  that the two strings should not have any common character. This
#  is taken care by creating a unique number for every string. 
#
#  Imagine a an 32 bit integer where 0 bit corresponds to 'a', 1st bit
#  corresponds to 'b' and so on.
#  Thus if two strings contain the same character when we do and
#  "AND" the result will not be zero and we can ignore that case.

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # create a mask to represent each word in words
        n = len(words)
        mask = [0] * n
        for i, w in enumerate(words):
            for c in w:
                mask[i] |= 1 << (ord(c) - ord('a'))
        maxProduct = 0
        for i in range (n):
            for j in range (i+1, n):
                if not mask[i] & mask[j]:
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
        return maxProduct

if __name__ == '__main__':
    sol = Solution()
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    assert sol.maxProduct(words) == 16

    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    assert sol.maxProduct(words) == 4

    words = ["a", "aa", "aaa", "aaaa"]
    assert sol.maxProduct(words) == 0

