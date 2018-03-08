# 320 Generalized Abbreviation
#
# Write a function to generate the generalized abbreviations of a word.
# 
# Example:
# 
# Given word = "word", return the following list (order does not matter):
# 
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", 
# "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

class Solution(object):
    def generateAbbreviations(self, word):
        def helper(word, pos, res):
            for i in range(pos, len(word)):
                j = 1
                while i+j <= len(word):
                    t = word[:i]
                    t = t + str(j) + word[i+j:]
                    res.append(t)
                    # 2 consecutive numbers are not allowed, skip 1
                    helper(t, i+1+len(str(j)), res)
                    j += 1
        res = ['word']
        helper(word, 0, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    exp = ["word","1ord","1o1d","1o2","1or1","2rd","2r1","3d","4","w1rd","w1r1","w2d","w3","wo1d","wo2","wor1"]
    assert sol.generateAbbreviations('word') == exp
