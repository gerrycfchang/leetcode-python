"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


"""
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root) + 1

    def dfs(self, node):
        if not node:
            return 0

        depth, leftcount, rightcount = 0, 0, 0
        if node.left is not None:
            leftcount = leftcount + self.dfs(node.left) + 1
        if node.right is not None:
            rightcount = rightcount + self.dfs(node.right) + 1
        depth = max(leftcount, rightcount)
        return depth