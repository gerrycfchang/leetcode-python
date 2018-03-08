# 314 Binary Tree Vertical Order Traversal
# 
# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left to right.
# 
# Examples:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its vertical order traversal as:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Given binary tree [3,9,20,4,5,2,7],
#     _3_
#    /   \
#   9    20
#  / \   / \
# 4   5 2   7
# return its vertical order traversal as:
# [
#   [4],
#   [9],
#   [3,5,2],
#   [20],
#   [7]
# ]

import sys
sys.path.append('../../')
from leetCodeUtil import TreeNode
from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        if not root: return []
        nodeQueue, res, table = [], [], defaultdict(list)
        nodeQueue.append([0, root])
        while len(nodeQueue) > 0:
            pair = nodeQueue.pop(0)
            seq, node = pair[0], pair[1]
            table[seq].append(node.value)
            if node.left:
                nodeQueue.append([seq-1, node.left])
            if node.right:
                nodeQueue.append([seq+1, node.right])
        for key in sorted(table.keys()):
            res.append(table[key])
        return res

if __name__ == '__main__':
    sol = Solution()
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
        [9],
        [3,15],
        [20],
        [7]
    ]
    assert sol.verticalOrder(root) == exp

    # Given binary tree [3,9,20,4,5,2,7],
    #     _3_
    #    /   \
    #   9    20
    #  / \   / \
    # 4   5 2   7
    root  = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(2)
    node7 = TreeNode(7)

    root.left = node1
    root.right = node2
    node1.left = node4
    node1.right = node5
    node2.left = node6
    node2.right = node7

    exp = [
       [4],
       [9],
       [3,5,2],
       [20],
       [7]
    ]
    assert sol.verticalOrder(root) == exp



