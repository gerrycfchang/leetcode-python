# 258. Add Digits
# 
# Given a non-negative integer num, repeatedly add all its digits 
# until the result has only one digit.
# 
# For example:
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num //=  10
            num = temp
        return num
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.addDigits(0) == 0
    assert sol.addDigits(38) == 2