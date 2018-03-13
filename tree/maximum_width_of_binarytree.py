# 662. Maximum Width of Binary Tree
#
# Given a binary tree, write a function to get the maximum width of the given tree. 
# The width of a tree is the maximum width among all levels. 
# The binary tree has the same structure as a full binary tree, but some nodes are null.
# 
# The width of one level is defined as the length between the end-nodes 
# (the leftmost and right most non-null nodes in the level, 
# where the null nodes between the end-nodes are also counted into the length calculation.
# 
# Input: 
# 
#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the 
# length 8 (6,null,null,null,null,null,null,7).


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        c, level = collections.defaultdict(list), 1
        self.inorder(root, level, 1, c)
        maxWidth = 0
        for value in c.values():
            maxWidth = max(maxWidth, value[-1] - value[0] + 1)            
        return maxWidth            
        
    def inorder(self, node, level, seq, c):
        if not node: return
        self.inorder(node.left, level + 1, 2*seq, c)
        c[level].append(seq)
        self.inorder(node.right, level + 1, (2*seq)+1, c)
        
if __name__ == '__main__':
    sol = Solution()
    
    """
            1
           / \
          2   2
         / \ / \
        3  4    3

    """
    node = TreeNode(1)
    leftNode = TreeNode(2)
    rightNode = TreeNode(2)
    node.left = leftNode
    node.right = rightNode

    thirdLevelLeftNode1 = TreeNode(3)
    thirdLevelLeftNode2 = TreeNode(4)
    thirdLevelRightNode1 = TreeNode(3)

    leftNode.left = thirdLevelLeftNode1
    leftNode.right = thirdLevelLeftNode2
    rightNode.right = thirdLevelRightNode1
    assert sol.widthOfBinaryTree(node) == 4
        
        