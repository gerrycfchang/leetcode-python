# 119. Pascal's Triangle II
# 
# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        if rowIndex == 0:
            return [1]
        for i in range(rowIndex+1):
            temp = [1 for x in range(i + 1)]
            result.append(temp)
            for j in range(1, i + 1):
                if j != 0 and j != i:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result[rowIndex]
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.getRow(3) == [1,3,3,1]
    assert sol.getRow(0) == [1]