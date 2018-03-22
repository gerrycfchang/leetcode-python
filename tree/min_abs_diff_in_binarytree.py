# 530. Minimum Absolute Difference in BST
# 
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
# 
# Example:
# 
# Input:
# 
#    1
#     \
#      3
#     /
#    2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.mindiff = float('inf') 
        Solution.prev = None
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            if Solution.prev:
                Solution.mindiff = min(Solution.mindiff, abs(node.val - Solution.prev.val))
            Solution.prev = node
            inorder(node.right)
        inorder(root)
        return Solution.mindiff

if __name__ == '__main__':
    sol = Solution()
    """
    #     1
    #      \
    #       3
    #      / 
    #     2   
    """
    root  = TreeNode(1)
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    root.right = node1
    node1.left = node2
    assert (sol.getMinimumDifference(root) == 1)

    """
    #     5
    #    /  \
    #   4    7 
    """
    root  = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(7)
    root.left = node1
    root.right = node2
    assert (sol.getMinimumDifference(root) == 1)
        
        