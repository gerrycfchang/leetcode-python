# 337. House Robber III
# 
# 
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
# 
# Example 1:
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return 0, 0
            YES_l, NO_l = dfs(node.left)
            YES_r, NO_r = dfs(node.right)
            return node.val + NO_l + NO_r, max(YES_l, NO_l) + max(YES_r, NO_r)
        
        return max(dfs(root))


if __name__ == '__main__':
    sol = Solution()
    """
    #           1
    #          / \
    #         3   2
    #        / \   \  
    #       5   3   9 
    """
    root  = TreeNode(1)
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(3)
    node5 = TreeNode(9)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    assert (sol.rob(root)) == 18


    #           4
    #          / 
    #         1   
    #        /     
    #       2 
    #      /
    #     3
    root  = TreeNode(4)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    root.left = node1
    node1.left = node2
    node2.left = node3
    assert (sol.rob(root)) == 7
      