# 669. Trim a Binary Search Tree
# 
# Given a binary search tree and the lowest and highest boundaries as L and R, 
# trim the tree so that all its elements lies in [L, R] (R >= L). 
# You might need to change the root of the tree, 
# so the result should return the new root of the trimmed binary search tree.
# 
# Example 1:
# Input: 
#     1
#    / \
#   0   2
# 
#   L = 1
#   R = 2
# 
# Output: 
#     1
#       \
#        2

import sys
sys.path.append('../')
from leetCodeUtil import TreeNode

class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if node:
                if node.value > R:
                    return trim(node.left)
                elif node.value < L:
                     return trim(node.right)
                else:
                    node.left = trim(node.left)
                    node.right = trim(node.right)
                    return node

        return trim(root)

if __name__ == '__main__':
    sol = Solution()
    root  = TreeNode(5)
    node1 = TreeNode(0)
    node2 = TreeNode(6)
    node3 = TreeNode(3)
    node4 = TreeNode(2)
    root.left = node1
    root.right = node2
    node1.right = node3
    node3.left = node4
    sol.trimBST(root, 2,5)
    res = root.getDFS(root)
    exp = [2, 3, 5]
    assert res == exp
