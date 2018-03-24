# 538. Convert BST to Greater Tree
# 
# Given a Binary Search Tree (BST), convert it to a Greater Tree 
# such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
# 
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.seqlist = []

    def __str__(self):
        self.inorder(self)
        return ' '.join(str(x) for x in self.seqlist)

    def inorder(self, curr):
        if not curr: return
        self.inorder(curr.left)
        self.seqlist.append(curr.val)
        self.inorder(curr.right)
        

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if not node: return
            inorder(node.right)
            node.val += self.total
            self.total = node.val
            inorder(node.left)
        self.total = 0
        inorder(root)
        return root


if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """

           5
         /   \
        2     13 
    """
    root1  = TreeNode(5)
    node11 = TreeNode(2)
    node12 = TreeNode(13)
    root1.left = node11
    root1.right = node12

    root2  = TreeNode(18)
    node21 = TreeNode(20)
    node22 = TreeNode(13)
    root2.left = node21
    root2.right = node22
    
    sol.convertBST(root1)
    assert str(root1) == str(root2)
        