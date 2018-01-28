"""
insert node to binary tree
"""
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode

class Solution(object):
    def insertBinaryTreeNode(self, root, node):
        treeNode = TreeNode(node)
        if root is None:
            return
        elif node < root.value:
            if root.left is None:
                root.left = treeNode
            else:
                self.insertBinaryTreeNode(root.left, node)
        elif node > root.value:
            if root.right is None:
                root.right = treeNode
            else:
                self.insertBinaryTreeNode(root.right, node)



