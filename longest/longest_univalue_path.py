# 687. Longest Univalue Path
#
# Given a binary tree, find the length of the longest path
# where each node in the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# Example 1:
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
# 2
#
# Example 2:
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
# 2
#
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = [0]

        def calculatePath(node):
            if node is None:
                return 0

            leftCount = calculatePath(node.left)
            rightCount = calculatePath(node.right)
            left, right = 0, 0

            if node.left and node.left.value == node.value:
                left = leftCount + 1

            if node.right and node.right.value == node.value:
                right = rightCount + 1

            res[0] = max(res[0], left + right)

            return max(left, right)

        calculatePath(root)
        return res[0]