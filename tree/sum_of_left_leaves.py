# 404. Sum of Left Leaves
# 
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def inorder(node, isLeft):
            if not node: return
            inorder(node.left, True)
            if not node.left and not node.right and isLeft:
                res.append(node.val)
            inorder(node.right, False)
        inorder(root, False)
        return sum(res)
        
if __name__ == '__main__':
    sol = Solution()
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root  = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    assert sol.sumOfLeftLeaves(root) == 24