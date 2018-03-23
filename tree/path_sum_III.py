# 437. Path Sum III
# 
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go downwards 
# 
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        preDict = collections.Counter([0])
        def dfs(p, target, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - target, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, preDict)
                dfs(p.right, target, pathSum, preDict)
                preDict[pathSum] -= 1
        dfs(root, sum, 0, preDict)
        return self.count
        
if __name__ == '__main__':
    sol = Solution()

    assert sol.pathSum(TreeNode(1), 1) == 1

    root = TreeNode(1)
    node1 = TreeNode(2)
    root.left = node1
    assert sol.pathSum(root, 2) == 1

    root = TreeNode(0)
    node1 = TreeNode(2)
    node2 = TreeNode(0)
    root.left = node1
    node1.right = node2
    assert sol.pathSum(root, 2) == 4

    #    0
    #   / \
    #  1   1
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    root.left = node1
    root.right = node2
    assert sol.pathSum(root, 1) == 4

    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1
    root  = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(-3)
    node3 = TreeNode(3)
    node4 = TreeNode(2)
    node5 = TreeNode(11)
    node6 = TreeNode(3)
    node7 = TreeNode(-2)
    node8 = TreeNode(1)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.right = node8

    assert sol.pathSum(root, 8) == 3

    #        5
    #      /   \
    #     4     8
    #    /     / \
    #   11    13  4
    #  / \       / \
    # 7   2     5   1
    root  = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(11)
    node4 = TreeNode(13)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(5)
    node9 = TreeNode(1)

    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9

    assert sol.pathSum(root, 22) == 3