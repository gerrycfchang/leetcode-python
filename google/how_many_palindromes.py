"""
write int howmanyPalindrome (string s)
"""
class Solution(object):
    def howmanyPalindrome(self, s):
        count = 0
        pstrlist = []
        for i in range (len(s)):
            count += self.countHelper(s, i, i, pstrlist)
            count += self.countHelper(s, i, i+1, pstrlist)
        print pstrlist
        return count

    def countHelper(self, s, begin, end, pstrlist):
        count = 0
        pstr = ''
        while begin >=0 and end < len(s) and s[begin] == s[end]:
            if begin == end:
                pstr += s[begin]
            else:
                pstr = s[begin]+pstr+s[end]
            pstrlist.append(pstr)
            count += 1
            begin -= 1
            end += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    
    assert sol.howmanyPalindrome('abbbac') == 10