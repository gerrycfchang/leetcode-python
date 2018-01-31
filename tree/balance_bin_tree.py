"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

import sys
sys.path.append('../')
from leetCodeUtil import TreeNode

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        leftDepth = self.dfs(root.left)
        rightDepth = self.dfs(root.right)
        return abs(leftDepth - rightDepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(self, node):
        if not node:
            return 0
        leftcount, rightcount = 0, 0
        if node.left is not None:
            leftcount = leftcount + self.dfs(node.left)
        if node.right is not None:
            rightcount = rightcount + self.dfs(node.right)

        return max(leftcount, rightcount)+1