# 112. Path Sum
# 
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such 
# that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
# 
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def inorder(node, value, sum):
            if not node: return False            
            if not node.left and not node.right and node.val+ value == sum:
                return True
            return inorder(node.right, value+node.val, sum) or inorder(node.left, value+ node.val, sum)         
        return inorder(root, 0, sum)
        

if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """
    Given binary tree [3,9,20,null,null,15,7],

           4
         /   \
        2      6
       / \    
      1   3  
    """
    root  = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(6)
    node3 = TreeNode(1)
    node4 = TreeNode(3)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    assert sol.hasPathSum(root, 9) == True