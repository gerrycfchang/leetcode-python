# 107. Binary Tree Level Order Traversal II
# 
# DescriptionHintsSubmissionsDiscussSolution
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (ie, from left to right, level by level from leaf to root).
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, c = [], collections.defaultdict(list)
        def inorder(curr, c, level):
            if not curr: return
            inorder(curr.left, c, level+1)
            c[level].append(curr.val)
            inorder(curr.right, c, level+1)
        inorder(root, c, 0)
        for i in reversed(range(len(c))):
            res.append(c[i])
        return res
            
if __name__ == '__main__':
    sol = Solution()
    """
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    """
    root  = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    exp = [
        [15, 7],
        [9, 20],
        [3]
    ]
    assert (sol.levelOrderBottom(root) == exp)
        