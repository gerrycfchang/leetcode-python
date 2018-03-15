# 103. Binary Tree Zigzag Level Order Traversal
# 
# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and # alternate between).# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
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
        for i in range(len(c)):
            if i % 2 == 0:
                res.append(c[i])
            else:
                res.append(c[i][::-1])
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
        [3],
        [20, 9],
        [15, 7]
    ]
    assert (sol.zigzagLevelOrder(root) == exp)