# 617. Merge Two Binary Trees
# 
# Given two binary trees and imagine that when you put one of them to cover the other, 
# some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
# then sum node values up as the new value of the merged node. Otherwise, 
# the NOT null node will be used as the node of new tree.
# 
# Example 1:
# Input: 
#   Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
#        3
#       / \
#      4   5
#     / \   \ 
#    5   4   7

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
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            node = TreeNode(t1.val+t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2

if __name__ == '__main__':
    sol = Solution()
    #           1                         2                             
    #          / \                       / \                            
    #         3   2                     1   3                        
    #        /                           \   \                      
    #       5                             4   7 

    root1  = TreeNode(1)
    node11 = TreeNode(3)
    node12 = TreeNode(2)
    node13 = TreeNode(5)
    root1.left = node11
    root1.right = node12
    node11.left = node13

    root2  = TreeNode(2)
    node21 = TreeNode(1)
    node22 = TreeNode(3)
    node23 = TreeNode(4)
    node24 = TreeNode(7)
    root2.left = node21
    root2.right = node22
    node21.right = node23
    node22.right = node24

    # Merged tree:
    #        3
    #       / \
    #      4   5
    #     / \   \ 
    #    5   4   7 

    exp  = TreeNode(3)
    node31 = TreeNode(4)
    node32 = TreeNode(5)
    node33 = TreeNode(5)
    node34 = TreeNode(4)
    node35 = TreeNode(7)
    exp.left = node31
    exp.right = node32
    node31.left = node33
    node31.right = node34
    node32.right = node35

    res = sol.mergeTrees(root1, root2)
    assert str(res) == str(exp)
        