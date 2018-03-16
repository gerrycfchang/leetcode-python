# 543. Diameter of Binary Tree
# refer to 
# 687. Longest Univalue Path
# 104. Maximum Depth of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path 
# between any two nodes in a tree. This path may or may not pass through the root.
# 
# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.maxLen = 0
        def inorder(curr):
            if not curr: return -1
            lcnt, rcnt = 0, 0
            lcnt = inorder(curr.left)
            rcnt = inorder(curr.right)
            if not curr.left or not curr.right:
                Solution.maxLen = max(max(lcnt, rcnt) + 1, Solution.maxLen)
            elif curr.left and curr.right:
                Solution.maxLen = max(lcnt + rcnt + 2, Solution.maxLen)         
            return max(lcnt,rcnt) + 1
        inorder(root)
        return Solution.maxLen   

if __name__ == '__main__':
    sol = Solution()
    
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    res = sol.diameterOfBinaryTree(root)
    assert (res == 3)

    #     1
    #    / 
    #   2   
    
    root  = TreeNode(1)
    node1 = TreeNode(2)

    root.left = node1
    res = sol.diameterOfBinaryTree(root)
    assert (res == 1)

    #     1
    #    / 
    #   2 
    #  / 
    # 3   
    
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)

    root.left = node1
    node1.left = node2
    res = sol.diameterOfBinaryTree(root)
    assert (res == 2)

    #     1
    #    / \
    #   2   3
    #  /   /
    # 4   5
    
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    res = sol.diameterOfBinaryTree(root)
    assert (res == 4)
        
        
            
        