# 124. Binary Tree Maximum Path Sum
# 
# Given a binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes 
# from some starting node to any node in the tree along the parent-child connections. 
# The path must contain at least one node and does not need to go through the root.
# 
# For example:
# Given the below binary tree,
# 
#        1
#       / \
#      2   3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        maxSum = [float('-inf')]
        self.inorder(root, maxSum)
        return maxSum[0]

    def inorder(self, node, maxSum):
        if not node: return 0
        if not node.left and not node.right:
            maxSum[0] = max(maxSum[0], node.val)
            return node.val
        leftValue = self.inorder(node.left, maxSum)
        rightValue = self.inorder(node.right, maxSum)
        maxSum[0] = max(maxSum[0], leftValue + node.val + rightValue, leftValue + node.val, rightValue + node.val, node.val)
        return max(leftValue+node.val, rightValue+node.val, node.val)

if __name__ == '__main__':
    sol = Solution()

    assert sol.maxPathSum(TreeNode(0)) == 0
    assert sol.maxPathSum(TreeNode(-3)) == -3

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
    assert sol.maxPathSum(root) == 47

    """
    #     2
    #    / 
    #   -1  
    """
    root  = TreeNode(2)
    node1 = TreeNode(-1)
    root.left = node1
    assert sol.maxPathSum(root) == 2

    """
    #    -2
    #    / 
    #   1  
    """
    root  = TreeNode(-2)
    node1 = TreeNode(1)
    root.left = node1
    assert sol.maxPathSum(root) == 1
        