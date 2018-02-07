"""
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".


"""

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        num = index = 0
        for w in abbr:
            if w.isdigit():
                num = num * 10 + int(w)
                if num > len(word):
                    return False
            else:
                index = num + index
                num = 0
                if index > len(word) or word[index] != w:
                    return False
                index += 1
        return index == len(word)


