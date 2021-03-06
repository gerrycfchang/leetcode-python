# 520. Detect Capital
# 
# Given a word, you need to judge whether the usage of capitals in it is right or not.
# 
# We define the usage of capitals in a word to be right when one of the following cases holds:
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > 1:
            if word.isupper() == True:
                return True
            elif word[0].isupper() == True and word[1:].islower() == True:
                return True
            elif word.islower() == True:
                return True
            else: return False
        return True
        
    def detectCapitalUseSol(self, word):
        return word.isupper() or word.islower() or word.istitle()
    
if __name__ == '__main__':
    sol = Solution()
    assert sol.detectCapitalUse('USA') == True
    assert sol.detectCapitalUse('FlaG') == False
    assert sol.detectCapitalUseSol('FlaG') == False