# 48. Rotate Image
# 
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.
# 
# Example 1:
# 
# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = [[matrix[row][col] for row in range(len(matrix)-1, -1, -1)] for col in range(len(matrix[0]))]
        

if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    exp = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]

    sol.rotate(matrix)
    assert matrix == exp