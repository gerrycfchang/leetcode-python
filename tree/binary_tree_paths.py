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
