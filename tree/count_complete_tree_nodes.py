# 222. Count Complete Tree Nodes
# 
# Given a complete binary tree, count the number of nodes.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, 
# is completely filled, and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        leftDepth = self.getDepth(root, True)
        rightDepth = self.getDepth(root, False)

        if leftDepth == rightDepth:
            return 2 ** leftDepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getDepth(self, node, isLeft):
        if not node: return 0
        if isLeft:
            return 1 + self.getDepth(node.left, isLeft)
        else:
            return 1 + self.getDepth(node.right, isLeft)


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
    assert sol.countNodes(root1) == 3

    ### Test case 2
    """

           5
         /  
        2      
    """
    root1  = TreeNode(5)
    node11 = TreeNode(2)    
    root1.left = node11
    assert sol.countNodes(root1) == 2