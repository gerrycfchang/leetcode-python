"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.


"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for x in range (len(s)-1,-1,-1):
            if x == len(s)-1:
                sum = sum + dic [s[x]]
            elif x > 0:
                if dic[s[x]] < dic[s[x+1]]:
                    sum = sum - dic[s[x]]
                else:
                    sum = sum + dic[s[x]]
            elif x == 0:
                if dic[s[x]] >= dic[s[x+1]]:
                    sum = sum + dic[s[x]]
                else:
                    sum = sum - dic[s[x]]
        return sum
