# 67. Add Binary
# 
# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100"# 

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.addBinary('11', '1') == '100'