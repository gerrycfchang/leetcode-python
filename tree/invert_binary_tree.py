"""
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""
from leetCodeUtil import TreeNode

class Solution(object):
    def invertTree(self, root):
        temp = TreeNode(-1)
        if root is None:
            return

        if root.left is not None or root.right is not None:
            temp = root.left
            root.left = root.right
            root.right = temp
        if root.left is not None:
            self.invertTree(root.left)
        if root.right is not None:
            self.invertTree(root.right)
        return root
