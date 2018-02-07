"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

"""
from collections import defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = defaultdict(set)
        for word in dictionary:
            abbr = self.getAbbr(word)
            if abbr not in self.dic:
                self.dic[abbr] = word
            else:
                if self.dic[abbr] != word:
                    self.dic[abbr] = ""
            """
            Solution 1:
            self.dic[abbr].add(word)
            """

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool

        Solution 1:
        abbr = self.getAbbr(word)
        return self.dic[abbr] <= {word}
        """
        abbr = self.getAbbr(word)
        if not (abbr in self.dic) or self.dic[abbr] == word:
            return True
        else:
            return False



    def getAbbr(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word)-2) + word[len(word)-1]





# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")