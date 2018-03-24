# 563. Binary Tree Tilt
# 
# Given a binary tree, return the tilt of the whole tree.
# 
# The tilt of a tree node is defined as the absolute difference 
# between the sum of all left subtree node values and the sum of all right subtree node values. 
# Null node has tilt 0.
# 
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# 
# Example:
# Input: 
#          1
#        /   \
#       2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tiltList = []
        def inorder(node):
            if not node: return 0
            leftSum = inorder(node.left)
            rightSum = inorder(node.right)
            total = leftSum + node.val + rightSum
            self.tiltList.append(abs(leftSum-rightSum))
            return total
        inorder(root)
        return sum(self.tiltList)

if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """
    Given binary tree [3,9,20,null,null,15,7],

           1
         /   \
        2     3 
    """
    root1  = TreeNode(1)
    node11 = TreeNode(2)
    node12 = TreeNode(3)
    root1.left = node11
    root1.right = node12
    assert sol.findTilt(root1) == 1
        
        