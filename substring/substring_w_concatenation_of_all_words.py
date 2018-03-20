# 30. Substring with Concatenation of All Words
# 
# You are given a string, s, and a list of words, words, that are all of the same length. 
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once 
# and without any intervening characters.
# 
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
# 
# You should return the indices: [0,9]. (order does not matter).

import collections
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res, wl = [], len(words[0])
        for i in range(wl):
            end = begin = i
            pStillNeed = collections.Counter(words)
            counter = len(pStillNeed)
            while end < len(s):
                w = s[end:end+wl]
                pStillNeed[w] -= 1
                if pStillNeed[w] == 0:
                    counter -= 1
                end += wl
                while counter == 0:                
                    tempw = s[begin:begin+wl]
                    if tempw in pStillNeed:
                        pStillNeed[tempw] += 1
                        if pStillNeed[tempw] > 0:
                            counter += 1                                                    
                    if end - begin == len(''.join(words)):
                        res.append(begin)
                    begin += wl
        return res

    def findSubstringPart2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        pStillNeed = collections.Counter(words)
        res, wl = [], len(words[0])
        for i in range(wl):
            begin = i
            end = i
            currDict = collections.Counter()
            while end + wl <= len(s):
                w = s[end:end+wl]
                end += wl 
                if w in pStillNeed:
                    currDict[w] += 1
                    while currDict[w] > pStillNeed[w]:
                        currDict[s[begin:begin+wl]] -= 1
                        begin += wl
                    if end - begin == len(''.join(words)):
                        res.append(begin)
                else:
                    currDict.clear()
                    begin = end
        return res

if __name__ == '__main__':
    sol = Solution()
    words = ["foo", "bar"]
    assert sol.findSubstring('barfoothefoobarman', words) == [0, 9]
    assert sol.findSubstringPart2('barfoothefoobarman', words) == [0, 9]
    words = ["bar","foo","the"]
    assert sol.findSubstring('barfoofoobarthefoobarman', words) == [6, 9, 12]
    assert sol.findSubstringPart2('barfoofoobarthefoobarman', words) == [6, 9, 12]
    words = ["aa","aa","aa"]
    assert sorted(sol.findSubstring('aaaaaaaa', words)) == [0, 1, 2]
    assert sorted(sol.findSubstringPart2('aaaaaaaa', words)) == [0, 1, 2]



