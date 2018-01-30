"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
"""

import sys
sys.path.append('../')
from leetCodeUtil import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.checkMirror(root.left, root.right)
        return True

    def checkMirror(self, p, q):
        if p is None and q is None:
            return True

        if p and q and p.value == q.value:
            return self.checkMirror(p.left, q.right) and self.checkMirror(p.right, q.left)
        else:
            return False
