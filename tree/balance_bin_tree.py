"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        leftDepth = self.dfs(root.left)
        rightDepth = self.dfs(root.right)
        return abs(leftDepth - rightDepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(self, node):
        if not node:
            return 0
        leftcount, rightcount = 0, 0
        if node.left is not None:
            leftcount = leftcount + self.dfs(node.left)
        if node.right is not None:
            rightcount = rightcount + self.dfs(node.right)

        return max(leftcount, rightcount)+1

if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """
    Given binary tree [3,9,20,null,null,15,7],

        1
         \
          2
           \
            3
    """
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)

    root.right = node1
    node1.right = node2

    assert (sol.isBalanced(root) == False)

    
    ### Test case 1
    """
    Given binary tree [1,2,2,3,null,null,3,4,null,null,4],

            1
           / \
          2   2
         /     \
        3       3
       /         \
      4           4
        """
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)

    root.left = node1
    root.right = node2
    node1.left = node3
    node2.right = node4
    node3.left = node5
    node4.right = node6

    assert (sol.isBalanced(root) == False)