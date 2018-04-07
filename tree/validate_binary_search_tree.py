# 98. Validate Binary Search Tree
# 
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        def inorder(node):
            if not node: return True            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res == sorted(res) and len(set(res)) == len(res)


if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """
    Given binary tree [3,9,20,null,null,15,7],

           2
         /   \
        1     3 
    """
    root1  = TreeNode(2)
    node11 = TreeNode(1)
    node12 = TreeNode(3)
    root1.left = node11
    root1.right = node12
    assert sol.isValidBST(root1) == True

    assert sol.isValidBST(TreeNode(0)) == True

    root1  = TreeNode(1)
    node12 = TreeNode(1)
    root1.right = node12
    assert sol.isValidBST(root1) == False