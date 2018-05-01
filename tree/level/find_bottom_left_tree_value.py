# 513. Find Bottom Left Tree Value
# 
# Given a binary tree, find the leftmost value in the last row of the tree.
# 
# Example 1:
# Input:
# 
#     2
#    / \
#   1   3
# 
# Output:
# 1
# Example 2: 
# Input:
# 
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# 
# Output:
# 7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import defaultdict
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node, level, dic):
            if not node: return
            inorder(node.left, level+1, dic)
            dic[level].append(node.val)
            inorder(node.right, level+1, dic)
        dic = defaultdict(list)
        inorder(root, 1, dic)
        return dic[max(dic.keys())][0]
        

if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """

           1
         /   \
        2     3 
    """
    root1  = TreeNode(1)
    node11 = TreeNode(2)
    node12 = TreeNode(3)
    root1.left = node11
    root1.right = node12
    assert sol.findBottomLeftValue(root1) == 2