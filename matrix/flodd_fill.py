# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image 
# (from 0 to 65535).
# 
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
# and a pixel value newColor, # "flood fill" the image.# 
# 
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of # the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels 
# (also with the same color as the starting pixel), and so on. 
# Replace the color of all of the aforementioned pixels with the newColor.# 
# 
# At the end, return the modified image.
# 
# Example 1:
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.dfs(sr, sc, image, image[sr][sc], newColor, visited)
        return image
        
    def dfs(self, i, j, image, value, newColor, visited):
        m = len(image)
        n = len(image[0])
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or image[i][j] != value:
            return
        image[i][j] = newColor
        visited[i][j] = True
        ## four directions
        self.dfs(i-1, j, image, value, newColor, visited)
        self.dfs(i+1, j, image, value, newColor, visited)
        self.dfs(i, j-1, image, value, newColor, visited)
        self.dfs(i, j+1, image, value, newColor, visited)
        
if __name__ == '__main__':
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    res = sol.floodFill(image, 1, 1, 2)

    exp = [[2,2,2],[2,2,0],[2,0,1]]
    assert  res == exp