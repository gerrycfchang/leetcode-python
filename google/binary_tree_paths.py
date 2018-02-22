"""

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        reslist = []
        if not root: return reslist

        def findNodePath(node, path):
            if node.left is None and node.right is None:
                reslist.append(path)
            if node.left:
                findNodePath(node.left, path + "->" + str(node.left.value))
            if node.right:
                findNodePath(node.right, path + "->" + str(node.right.value))

        findNodePath(root, str(root.value))
        return reslist

import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
if __name__ == '__main__':
    """
        Given binary tree [3,9,20,null,null,15,7],

            1
           / \
          2   3
            \
            5
        """
    ## case 1
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.right = node3
    sol = Solution()
    result = sol.binaryTreePaths(root)
    exp = ["1->2->5", "1->3"]

    result.sort()
    exp.sort()
    assert result==exp

    ## case 2
    root = None
    result = sol.binaryTreePaths(root)
    assert result==[]