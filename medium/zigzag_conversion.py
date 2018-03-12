# 6. ZigZag Conversion
# 
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".# 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        L = ['' for _ in range(numRows)]
        index, step = 0, 0
        if len(s) <= numRows or numRows == 1: return s
        for c in s:
            L[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)

if __name__ == '__main__':
    sol = Solution()
    assert sol.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'