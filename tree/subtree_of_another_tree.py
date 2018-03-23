# 572. Subtree of Another Tree
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values 
# with a subtree of s. 
# A subtree of s is a tree consists of a node in s and all of this node's descendants. 
# The tree s could also be considered as a subtree of itself.
# 
# Example 1:
# Given tree s:
# 
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
# 
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isMatch(s, t):
            if not s or not t: return s is t
            return (s.val == t.val and 
            isMatch(s.left, t.left) and
            isMatch(s.right, t.right))
        if not s: return False
        if isMatch(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
                
if __name__ == '__main__':
    sol = Solution()
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    root  = TreeNode(3)
    node1 = TreeNode(4)
    node2 = TreeNode(5)
    node3 = TreeNode(1)
    node4 = TreeNode(2)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    sub1 = TreeNode(4)
    sub2 = TreeNode(1)
    sub3 = TreeNode(2)
    
    sub1.left = sub2
    sub1.right = sub3
    assert sol.isSubtree(root, sub1) == True