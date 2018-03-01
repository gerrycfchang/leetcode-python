"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        if numRows == 0:
            return result

        for i in range(numRows):
            temp = [1 for x in range(i + 1)]
            result.append(temp)
            for j in range(1, i + 1):
                if j != 0 and j != i:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

        return result

if __name__ == '__main__':
    sol = Solution()
    
    exp = [[1],[1,1],[1,2,1],[1,3,3,1]]
    assert (sol.generate(4) == exp)

    exp = [[1]]
    assert (sol.generate(1) == exp)
