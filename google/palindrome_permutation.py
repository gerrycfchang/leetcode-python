"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?

"""

class Solution(object):
    def canPermutePalindrome(self, str):

        ### Solution 1:
        if not str:
            return False
        table = {}

        for s in str:
            if s in table:
                table[s] += 1
            else:
                table[s] = 1
        sum = 0

        for key, value in table.iteritems():
            if value % 2 != 0:
                sum += 1
        return sum < 2

        """
        Solution 2:
        from collections import Counter
        c = Counter(str)
        sum = 0
        for value in c.values():
            if value % 2 != 0:
                sum += 1
        return sum < 2
        """

if __name__ == '__main__':
    sol = Solution()
    assert sol.canPermutePalindrome('code') == False
    assert sol.canPermutePalindrome('aab') == True
    assert sol.canPermutePalindrome('carerac') == True
